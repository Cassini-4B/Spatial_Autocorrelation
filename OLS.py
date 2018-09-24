import pandas as pd
import numpy as np
from pysal.spreg import ols
from pysal.spreg import ml_error
from pysal.spreg import ml_lag
import pysal
from pysal import W

def std_OLS(datafile):
	f = pysal.open(datafile)
	y = np.array(f.by_col[dependent_variable])
	X = []
	X.append(datafile[[independent_variables]])
	X = np.array(X).T

	ls = ols.OLS(y, X, name_y = 'variable_name', name_x = ['independent_variables'])
	
	return (ls.summary)


