# Imports
import warnings
warnings.filterwarnings("ignore",category=UserWarning)
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import glob,os
from tqdm.auto import tqdm
import math
import sklearn
from sklearn.linear_model import LinearRegression
import pickle

import tigramite
from tigramite import data_processing as pp
from tigramite.toymodels import structural_causal_processes as toys
from tigramite.models import Models, Prediction
from tigramite import plotting as tp
from tigramite.pcmci import PCMCI
from tigramite.independence_tests import ParCorr, GPDC, CMIknn, CMIsymb

def select_links(tau_min, tau_max, parents, children):
    """
    This function selects the causal links that will be tested by
    PCMCI. The links are selected such that per each variable in
    `children` all `parents` are stablished as causes, and no other
    causal relationships exist.
    
    Assumes `parents` and `children` are disjoint sets, and that all
    variables are included in the union of both sets.
    
    Parameters
    ----------
    tau_min : int
        Minimum time lag to test. Note that zero-lags are undirected.
    tau_max : int
        Maximum time lag. Must be larger or equal to tau_min.
    parents : set of int
        List of variables that will be assigned as a parent link.
        Assumed to be disjoint with children
    children : set of int
        List of variables that will be assigned a link from a parent.
        Assumed to be disjoint with parents
    Returns
    -------
    selected_links: dict
        Dictionary of selected links for Tigramite
        
    """

    parents = set(parents)
    children = set(children)

    selected_links = dict()
    # Set the default as all combinations of the selected variables
    for var in [*children, *parents]:
        if var in children:
            # Children can be caused only by parents and by themselves
            selected_links[var] = [
                (parent, -lag)
                for parent in parents
                for lag in range(tau_min, tau_max + 1)
            ]
        else:
            selected_links[var] = []

    return selected_links

def _process_dataset(path=None):
    df1 = pd.read_csv(path,sep=',')
    df1.rename({"Unnamed: 0":"a"}, axis="columns", inplace=True)
    df1=df1.drop('a', axis=1)
    df1=df1.drop('conv_rrate', axis=1)
    df1=df1.drop('ls_rrate', axis=1)
    df1=df1.drop('mn_conv_prate', axis=1)
    df1=df1.drop('mn_ls_prate', axis=1)
    df1=df1.drop('mn_tot_prate', axis=1)
    df1=df1.drop('outconv_rrate', axis=1)
    df1=df1.drop('outls_rrate', axis=1)
    df1=df1.drop('outmn_conv_prate', axis=1)
    df1=df1.drop('outmn_ls_prate', axis=1)
    df1=df1.drop('outmn_tot_prate', axis=1)
    df1=df1.drop('conv_ppt', axis=1)
    df1=df1.drop('outconv_ppt', axis=1)
    
    TCname = path.split('/')[-1].split('.')[0].split('_')[-1]
    #print(TCname)
    for item in glob.glob('/work/FAC/FGSE/IDYST/tbeucler/default/saranya/causal/targets/*tot_ppt_int*'):
        if str(TCname) in item:
            d1=pd.read_csv(item)
            d1.rename({"Unnamed: 0":"a"}, axis="columns", inplace=True)
            d1=d1.drop('a', axis=1)
            dt1=pd.concat([d1,df1],axis=1, join='inner')
        else:
            continue
    return dt1

class Pipeline:
    """
    Tigramite and Linear Regression Pipeline
    """
    def __init__(self,data,pc_alpha,alpha_level,pc_type='run_pcstable' or 'pcmci',tau_min0=None,tau_max0=None,
                 target='precip',var_name=None,seed=None,cond_ind_test=ParCorr()):
        self.pc_alpha = pc_alpha
        self.alpha_level = alpha_level
        self.data = data
        self.pc_type = pc_type
        self.target = target
        self.tau_min0 = tau_min0
        self.tau_max0 = tau_max0
        self.var_name = var_name
        self.seed = seed
        self.cond_ind_test = cond_ind_test
        
    #################################################################################
    # Step 0: Split
    #################################################################################
    def splitdata(self,testindex=None):
        datae = self.data.copy()
        traindata = {}
        testdata = {}
        validdata = {}
        validindex,newtestindex = testindex[:int(len(testindex)/2)],testindex[int(len(testindex)/2):]
        for obj in datae.keys():
            number = (obj)
            if number in list(newtestindex):
                testdata[str(number)] = datae[(number)]
            elif number in list(validindex):
                validdata[str(number)] = datae[(number)]
            else:
                traindata[str(number)] = datae[(number)]
        return traindata,validdata,testdata
    
    #################################################################################
    # Step 1: Tigramite
    #################################################################################
    def run_tigramite(self,lengthtrain=None):
        #assert len(self.data)==lengthtrain,"Wrong shape!"
        datae = self.data.copy()
        dataframe =  pp.DataFrame(datae,analysis_mode ='multiple', var_names=self.var_name,missing_flag=-999.)
        #################################################################################
        # Sel links
        #################################################################################
        for member in dataframe.values.keys():
            children = [0,1,2]
            parents = np.arange(0,234)
            sel_links = select_links(self.tau_min0, self.tau_max0, parents, children)
        #################################################################################
        # Run Tigramite
        #################################################################################        
        pcmci = PCMCI(dataframe = dataframe, cond_ind_test = self.cond_ind_test)
        if self.pc_type=='run_pcstable':
            results = pcmci.run_pc_stable(selected_links=sel_links, tau_min=self.tau_min0, tau_max=self.tau_max0,\
                                          pc_alpha=self.pc_alpha)
        elif self.pc_type=='pcmci':
            results = pcmci.run_pcmci(selected_links=sel_links, tau_min=self.tau_min0, tau_max=self.tau_max0,\
                                      pc_alpha=self.pc_alpha)

        pcmci.verbosity = 2
        #################################################################################
        # Test
        #################################################################################   
        #pcmci.print_results(results,self.alpha_level)
        #pcmci.print_significant_links(p_matrix=results['p_matrix'],
        #val_matrix = results['val_matrix'],
        #alpha_level = self.alpha_level)
        return results
    
    #################################################################################
    # Step 2: Linear Regression
    #################################################################################
    # Helper functions
    #################################################################################
    def random_testindex(self,totalexp=None,testexp=None):
        from numpy.random import default_rng
        rng = default_rng(self.seed)
        seed = rng.choice(totalexp, testexp, replace=False)
        return seed
    
    def extract_lag_info(self,datar=None,varindex=None,lag=None):
        temp = datar[:,varindex] # Full time series
        store = []
        for timeindex in range(len(temp)):
            if timeindex < np.abs(lag):
                store.append(np.nan)
            elif timeindex > len(temp)-1-np.abs(lag):
                store.append(np.nan)
            else:
                store.append(temp[timeindex-np.abs(lag)])
        return store
    
    def extract_var_and_lag(self,pcmci_results=None,p_or_q='p' or 'q'):
        datae = self.data.copy()
        dataframe =  pp.DataFrame(datae,analysis_mode ='multiple',var_names=self.var_name,missing_flag=-999.)
        pcmci = PCMCI(dataframe = dataframe, cond_ind_test = self.cond_ind_test)
        #################################################################################
        # Sel links
        #################################################################################
        for member in dataframe.values.keys():
            children = [0,1,2]
            parents = np.arange(0,234)
            sel_links = select_links(self.tau_min0, self.tau_max0, parents, children)
        
        q_matrix = pcmci.get_corrected_pvalues(p_matrix=pcmci_results['p_matrix'],
                                               selected_links = sel_links, 
                                               tau_min=self.tau_min0,tau_max=self.tau_max0, fdr_method='fdr_bh')
        #################################################################################
        # Save vars and lags
        #################################################################################
        if p_or_q=='p':
            sig_links = (pcmci_results['p_matrix'].copy() <= self.alpha_level)
        elif p_or_q=='q':
            sig_links = (q_matrix.copy() <= self.alpha_level)
        arr = []
        for j in range(3):
            links = {(p[0], -p[1]): np.abs(pcmci_results['val_matrix'][p[0],j,abs(p[1])]) for p in zip(*np.where(sig_links[:,j,:]))}
            # Sort by value
            sorted_links = sorted(links, key=links.get, reverse=True)
            arr.append(sorted_links)
        return arr
    
    #################################################################################
    # Process functions
    #################################################################################
    def preproc_ts_withnan(self,links=None,group=None,trainmean=None,trainstd=None):
        if self.target=='precip':
            arrtarget,ytarget = links[0],[self.data[obj][:,0] for obj in self.data.keys()]
        elif self.target=='pmin':
            arrtarget,ytarget = links[1],[self.data[obj][:,1] for obj in self.data.keys()]
        elif self.target=='v10':
            arrtarget,ytarget = links[2],[self.data[obj][:,2] for obj in self.data.keys()]
        
        # 1. Extract time series with nan
        varindexstore,lagstore,TS_store,flatTS_store = [],[],[],[]
        for varindex,lag in arrtarget:
            varindexstore.append(varindex)
            lagstore.append(lag)
            tempp = [self.extract_lag_info(datar=self.data[obj],varindex=varindex,lag=lag) for obj in self.data.keys()]
            TS_store.append(tempp)
            flatTS_store.append(np.concatenate([obj for obj in tempp]))
        
        # 2. Normalize
        if group=='train':
            TSnorml_store,meanstore,stdstore = [],[],[]
            for i in range(len(TS_store)): #combination
                tempmean,tempstd = np.nanmean(flatTS_store[i]),np.nanstd(flatTS_store[i])
                TSnorml_store.append([(obj-tempmean)/tempstd for obj in TS_store[i]])
                meanstore.append(tempmean)
                stdstore.append(tempstd)
        elif (group=='test') or (group=='valid'):
            TSnorml_store = []
            for i in range(len(TS_store)):
                tempmean,tempstd = (trainmean[i]),(trainstd[i])
                TSnorml_store.append([(obj-tempmean)/tempstd for obj in TS_store[i]])
            
        # 3. Concatenate
        #validindex,testindex = validtestindex[0:int(np.round(len(validtestindex)/2))],\
        #validtestindex[int(np.round(len(validtestindex)/2)):]
        
        Xtrain_withnan_store = []
        for i in range(len(TS_store)):
            storelist = [i for j, i in enumerate(TSnorml_store[i])]
            Xtrain_withnan_store.append(np.concatenate([obj for obj in storelist]))
            
        Ytrain = np.concatenate([i for j, i in enumerate(ytarget)])
        if group=='train':
            return Xtrain_withnan_store,Ytrain,meanstore,stdstore
        elif group=='valid':
            return Xtrain_withnan_store,Ytrain
        elif group=='test':
            return Xtrain_withnan_store,Ytrain
    
    def remove_nan(self,Xdict=None,ydict=None):
        def _remove_nan(X=None,y=None):
            X_nonan,Y_nonan = [],[]
            X_withnan_storer = np.asarray(X).transpose()
            for i in (range(len(y))):
                tempX = X_withnan_storer[i,:]
                if np.isnan(tempX).any():
                    continue
                else:
                    X_nonan.append(tempX)
                    Y_nonan.append(y[i])
            return X_nonan,Y_nonan
        Xtrain,ytrain = _remove_nan(X=Xdict['train'],y=ydict['train'])
        Xvalid,yvalid = _remove_nan(X=Xdict['valid'],y=ydict['valid'])
        Xtest,ytest = _remove_nan(X=Xdict['test'],y=ydict['test'])
        Xnewtest,ynewtest = _remove_nan(X=Xdict['newtest'],y=ydict['newtest'])
        return {'train':Xtrain,'valid':Xvalid,'test':Xtest,'newtest':Xnewtest},{'train':ytrain,'valid':yvalid,'test':ytest,'newtest':ynewtest}

    def remove_999(self,Xdict=None,ydict=None):
        def _remove_999(X=None,y=None):
            X_nonan,Y_nonan = [],[]
            X_withnan_storer = np.asarray(X).transpose()
            for i in (range(len(y))):
                tempX = X_withnan_storer[i,:]
                if y[i]==-999.:
                    continue
                else:
                    X_nonan.append(tempX)
                    Y_nonan.append(y[i])
            return X_nonan,Y_nonan
        Xtrain,ytrain = _remove_999(X=Xdict['train'],y=ydict['train'])
        Xvalid,yvalid = _remove_999(X=Xdict['valid'],y=ydict['valid'])
        Xtest,ytest = _remove_999(X=Xdict['test'],y=ydict['test'])
        Xnewtest,ynewtest = _remove_999(X=Xdict['newtest'],y=ydict['newtest'])
        return {'train':Xtrain,'valid':Xvalid,'test':Xtest,'newtest':Xnewtest},{'train':ytrain,'valid':yvalid,'test':ytest,'newtest':ynewtest}
    #################################################################################
    # Train model
    #################################################################################
    def train_mlr(self,X=None,y=None):
        regr = LinearRegression()
        regr.fit(X['train'],y['train'])
        return regr
    
def trainMLR_target(traindata=None,validdata=None,testdata=None,newtestdata=None,pc_alpha=None,alpha_level=None,tau_min0=None,tau_max0=None,
                    var_names=None,target='precip' or 'pmin' or 'v10',seed=12345,var_and_lag=None):
    ################################################################################################################
    # 1. X,y with nan
    Xtrain_nan,ytrain_nan,trainmean,trainstd = Pipeline(traindata,pc_alpha,alpha_level,pc_type='pcmci',\
                                                        tau_min0=tau_min0,tau_max0=tau_max0,\
                                                        target=target,var_name=var_names,\
                                                        seed=seed).preproc_ts_withnan(links=var_and_lag,group='train',\
                                                                                       trainmean=None,trainstd=None)
    Xvalid_nan,yvalid_nan = Pipeline(validdata,pc_alpha,alpha_level,pc_type='pcmci',\
                                   tau_min0=tau_min0,tau_max0=tau_max0,target=target,\
                                   var_name=var_names,seed=seed).preproc_ts_withnan(links=var_and_lag,\
                                                                                     group='valid',\
                                                                                     trainmean=trainmean,\
                                                                                     trainstd=trainstd)
    
    Xtest_nan,ytest_nan = Pipeline(testdata,pc_alpha,alpha_level,pc_type='pcmci',\
                                   tau_min0=tau_min0,tau_max0=tau_max0,target=target,\
                                   var_name=var_names,seed=seed).preproc_ts_withnan(links=var_and_lag,\
                                                                                     group='test',\
                                                                                     trainmean=trainmean,\
                                                                                     trainstd=trainstd)
    Xnewtest_nan,ynewtest_nan = Pipeline(newtestdata,pc_alpha,alpha_level,pc_type='pcmci',\
                                         tau_min0=tau_min0,tau_max0=tau_max0,target=target,\
                                         var_name=var_names,seed=seed).preproc_ts_withnan(links=var_and_lag,\
                                                                                          group='test',\
                                                                                          trainmean=trainmean,\
                                                                                          trainstd=trainstd)
    X_nan = {'train':Xtrain_nan,'valid':Xvalid_nan,'test':Xtest_nan,'newtest':Xnewtest_nan}
    y_nan = {'train':ytrain_nan,'valid':yvalid_nan,'test':ytest_nan,'newtest':ynewtest_nan}
    ################################################################################################################
    # 2. remove nan
    X_nonan,y_nonan = Pipeline(traindata,pc_alpha,alpha_level,pc_type='pcmci',\
                               tau_min0=tau_min0,tau_max0=tau_max0,target=target,\
                               var_name=var_names,seed=seed).remove_nan(Xdict=X_nan,ydict=y_nan)
    ################################################################################################################
    # 3. Train MLR
    wpac_mlr = Pipeline(traindata,pc_alpha,alpha_level,pc_type='pcmci',\
                        tau_min0=tau_min0,tau_max0=tau_max0,target=target,\
                        var_name=var_names,seed=seed).train_mlr(X=X_nonan,y=y_nonan)
    ################################################################################################################
    return wpac_mlr,X_nonan,y_nonan

def save_to_pickle(loc=None,var=None):
    with open(loc,"wb") as f:
        pickle.dump(var,f)
    return None

def depickle(loc=None):
    output = []
    with open(loc,'rb') as f:
        output.append(pickle.load(f))
    return output[0]

def flatten(l):
    return [item for sublist in l for item in sublist]

def do_num_to_nan(data=None):
    newdata = {}
    for intt,obj in enumerate(data.keys()):
        temp = data[obj].copy()
        temp[temp==-999.] = np.nan
        newdata[obj] = temp
    return newdata

def nan_to_999(dictionary=None):
    newdict = {}
    for name in dictionary.keys():
        newdict[name] = np.nan_to_num(dictionary[name].copy(),-999)
    newdict2 = {}
    for name in newdict.keys():
        temp = newdict[name].copy()
        temp[temp==0] = -999.
        newdict2[name] = temp
    return newdict2

