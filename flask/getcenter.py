import folium
import pandas as pd

# use this center the folium map based on dataset

def findcenter(file):
    centercoords = []
    data = pd.read_csv(file, sep=',', header=0)
    centerlat = data['Lat'].median()
    centerlong = data['Long'].median()
    centercoords.append(centerlat)
    centercoords.append(centerlong)
    
    return centercoords