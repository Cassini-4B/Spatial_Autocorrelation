import pandas as pd
import numpy as np
import pysal
from pysal import W

def get_local_moran(neighbors, datafile):
	w = W(neighbors)
	y = datafile['target_variable']
	lm = pysal.Moran_Local(y,w)
	
	significant_mI = lm.p_sim<0.05
	hotspots = lm.q == 1 * sig
	coldspots = lm.q == 3 * sig

	return datafile[hotspots], datafile[coldspots]
	
