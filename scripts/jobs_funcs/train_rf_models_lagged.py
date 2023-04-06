import numpy as np
import pandas as pd
import numpy as np
import pickle
import math
import sklearn
import glob
from tqdm.auto import tqdm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import RandomizedSearchCV
import itertools
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score,mean_squared_error
import sys
import func

def fit_rf(random_grid=None,estimator=None,X=None,y=None):
    rf = RandomForestRegressor()
    rf_random = RandomizedSearchCV(estimator=rf,param_distributions=random_grid,n_iter=50,cv=3,verbose=2,random_state=42,n_jobs=-1)
    rf_random.fit(X,y)
    return rf_random


script_name = sys.argv[0]
linkname = str(sys.argv[1])

seedname=12348
# Random Forest RandomSearch
n_estimators = [int(x) for x in np.linspace(100,500,5)]
max_features = ['auto']
max_depth = [int(x) for x in np.linspace(10,110,6)]
#max_depth.append(None)
min_samples_split = [int(x) for x in np.linspace(20,120,6)]
min_samples_leaf = [int(x) for x in np.linspace(20,120,6)]
bootstrap = [True]

random_grid = {'n_estimators':n_estimators,
               'max_features':max_features,
               'max_depth':max_depth,
               'min_samples_split':min_samples_split,
               'min_samples_leaf':min_samples_leaf,
               'bootstrap':bootstrap}

files = sorted(glob.glob('/work/FAC/FGSE/IDYST/tbeucler/default/saranya/causal/causal_notebooks/climateinformatics_revision1//store/lag/12348/lag*8_24*v10.obj.'+linkname))[0]
file = func.depickle(files)
rf_mdl = fit_rf(random_grid,RandomForestRegressor(),file['X']['train'],file['y']['train'])
tosave = {'model':rf_mdl,'X':file['X'], 'y':file['y']}

func.save_to_pickle(loc='/work/FAC/FGSE/IDYST/tbeucler/default/saranya/causal/causal_notebooks/climateinformatics_revision1/store/lag_rf/lagrf_8-24_v10.obj.'+linkname+'.'+str(seedname),var=tosave)
del files,file,rf_mdl
print('__Finish!!!!!__')
