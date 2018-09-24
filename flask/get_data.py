import csv
import pandas as pd


def get_csv_heatdata(file):
    data = pd.read_csv(file, sep=',', header=0)
    heat_data = [[row['Lat'], row['Long'], row['rate']] for index, row in data.iterrows()]    

    return heat_data