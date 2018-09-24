import pandas as pd
import csv
import pickle


# use this to get neighboring counties to calculate spatial matrix for Moran's I  

def get_neighbor_matrix(file):
    neighbors = pd.read_pickle('allneighbors.pickle')
    data = pd.read_csv(file, sep=',', header=0)
    subneighbors = {}
    for c in data['County']:
        subneighbors[c]=neighbors[c]

    return subneighbors




