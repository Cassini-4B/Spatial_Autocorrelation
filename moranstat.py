import pandas as pd
import csv
import numpy as np
import pysal
from pysal import W


def get_moran(neighbors, datafile):
	w = W(neighbors)
	y = datafile['target_variable']
	mi = pysal.Moran(y, w, two_tailed=True)
	
	MoransI = mi.I
	Expected_value = mi.EI
	pvalue = mi.p_norm

	return MoransI, Expected_value, pvalue
	

