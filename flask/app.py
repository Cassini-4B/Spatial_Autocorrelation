# app.py

import os
import requests
from flask import Flask, request, redirect, render_template
from flask import send_from_directory
from flask_uploads import UploadSet, configure_uploads, IMAGES
from getcenter import findcenter
from get_data import get_csv_heatdata
from get_moran import sp_dep, get_exp_plot, get_moran_plot
from getneighbors import get_neighbor_matrix
import numpy as np


# create a flask object
app = Flask(__name__)



# creates an association between the / page and the entry_page function (defaults to GET)
@app.route('/')
def entry_page():
    return render_template('index.html')



# creates an association between the /predict_recipe page and the render_message function
# (includes POST requests which allow users to enter in data via form)
@app.route('/mapmoran/', methods=['GET', 'POST'])


def show_spatial_data_corr():
    # retrieve csv file from input
    input_file = request.form['geodata']

    # create heatmap of data
    mapcenter = findcenter(input_file)
    mapdata = get_csv_heatdata(input_file)
    
    # calculate Moran's I and Expected I 
    number = str(np.random.randint(0,100))
    spatialmatrix = get_neighbor_matrix(input_file)
    get_moran_plot(sp_dep(input_file, spatialmatrix), number)
    get_exp_plot(sp_dep(input_file, spatialmatrix), number)
       
    return render_template('moranmap.html', centerpt = mapcenter, map=mapdata, id=number)




if __name__ == '__main__':
	#app.run(debug=True)
	app.run()


