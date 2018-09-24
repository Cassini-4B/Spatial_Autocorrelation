import pandas as pd  
import numpy as np  
import csv 
import seaborn as sns
import matplotlib.pyplot as plt  
import pickle
import pysal
from pysal import W


def sp_dep(data, spatial_neighbors):

    data = pd.read_csv(data, sep=',', header=0)
    y=data['rate']
    
    w = W(spatial_neighbors)
    mi = pysal.Moran(y, w, two_tailed=True)

    return (mi)


def get_moran_plot(spatial_stat, idname):
    sns.kdeplot(spatial_stat.sim, shade=True)
    plt.vlines(spatial_stat.sim, 0, 1)
    plt.vlines(spatial_stat.I+.01, 0, 10, 'r')
    plt.title("Moran's I and KDE")
    plt.text(.05, 4.75, "Moran's I: %.5f"%spatial_stat.I)
    plt.text(.05, 4.5, "p-value: %.5f"%spatial_stat.p_norm)
    plt.savefig(f'/home/sangrador/Metis/Bootcamp/Week9/Project5/flask/static/mi{idname}.png')
    plt.close()



def get_exp_plot(spatial_stat, idname):
    sns.kdeplot(spatial_stat.sim, shade=True)
    plt.vlines(spatial_stat.sim, 0, 1)
    plt.vlines(spatial_stat.EI+.01, 0, 10, 'r')
    plt.text(.05, 4.5, 'Expected I: %.5f'%spatial_stat.EI)
    plt.title("Expected KDE (no spatial dependencies)")
    plt.savefig(f'/home/sangrador/Metis/Bootcamp/Week9/Project5/flask/static/exp{idname}.png')
    plt.close()
