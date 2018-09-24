import pandas as pd
import numpy as np
from pysal.spreg import ols
from pysal.spreg import ml_error
from pysal.spreg import ml_lag
import pysal
from pysal import W

def spatial_lag_regression(datafile):
	f = pysal.open(datafile)
	y = np.array(f.by_col[dependent_variable])
	X = []
	X.append(datafile[[independent_variables]])
	X = np.array(X).T

	lag=pysal.spreg.ML_Lag(y, X, w,  name_y='dependent_variable', name_x=['independent_variable_names'])

	
	return (lag.summary)
