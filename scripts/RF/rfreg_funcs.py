# Imports
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
from sklearn.inspection import permutation_importance
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor

def train_rf(n_estimators=None,max_features=None,max_depth=None,min_samples_split=None,
             min_samples_leaf=None,bootstrap=None,X=None,y=None):
    rf =  RandomForestRegressor(n_estimators=n_estimators,max_features=max_features,max_depth=max_depth,
                                 min_samples_split=min_samples_split,min_samples_leaf=min_samples_leaf,bootstrap=bootstrap)
    return rf.fit(X,y)

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

def _get_importance_ranking(model=None,TYPE=None,index=None,X=None,y=None):
    if TYPE=='gini':
        forest_importances_gini = pd.Series(model.feature_importances_,index=flatten(index))
        return forest_importances_gini
    elif TYPE=='permutation':
        result = permutation_importance(model,X['test'],y['test'])
        forest_importances = pd.Series(result.importances_mean,index=flatten(index))
        return forest_importances

def sorted_importance(importances=None):
    dff = importances.to_frame(name='Importance')
    dff = dff.reset_index()
    dff.columns = ['Combination','Importance']
    dff['Importance_abs'] = np.abs(dff['Importance'])
    dff['rank'] = dff['Importance_abs'].rank(ascending=False)
    dff_pmin_sorted = dff.sort_values(by='rank').reset_index()
    return dff_pmin_sorted