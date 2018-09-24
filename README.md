# Spatial_Autocorrelation

This project is about detecting spatial autocorrelation in your data.

## What is spatial autocorrelation?

Spatial autocorrelation is something to consider when you have data that has a spatial component to it.  It basically involves the idea that there is a relationship or association of a variable with itself in nearby areas.  Data tends to be similar in areas that are geographically located close to each other, but data tends to be different or have a higher range in areas that are further apart.  Say, for example, you are looking at trends or topics in social media.  You will find higher occurances of the topic 'Brexit' in the UK and Europe, but less so in the US.  Spatial autocorrelation looks at these relationships and provides a quantitative way to measure the extent of these associations.

Spatial autocorrelation also helps to determine if there are any spatial patterns to your data.  Positive autocorrelation means that there are patterns of similarity, or spatial clustering in your dataset.  Negative autocorrelation means that there are patterns of dissimilarity in your dataset.  This is a quick and easy way to visually perform exploratory data analysis (EDA) on your data.  

## Why does spatial autocorrelation matter?

If your model is not taking spatial autocorrelation into account, then these relationships become hidden as a latent variable in your error.  So at the very least, you'll have higher errors in your model and won't be capturing all the variance present in your data.  But you could also be using a model that is misleading--you could have a biased model, where the relationships between the dependent and independent variables appear to be greater than they really are because what's really influencing the relationship is actually the location, and not just the features themselves.  

## Solution

The objective of this project was to create an app that will help detect spatial autocorrelation in your data to help mitigate these issues.  It's very simple and easy to implement.  All you need is:

1) CSV file of your data with latitude and longitude coordinates of your observations
2) neighbors file ('allneighbors.pickle' listed in getneighbors.py file).  This file is a dictionary of each observation's geographic location and its neighbors.  For example if you were looking at county level data, then this file would contain each county as a key and it's variables would be every adjacent county that shared a border with it in the state.  You can also choose to use a distance threshold to determine neighbors.
3) In order to display the map of your data, you will need leaflet (https://leafletjs.com/) and folium (https://github.com/python-visualization/folium).

I have chosen to use Moran's I (https://en.wikipedia.org/wiki/Moran%27s_I) as the statistic to calculate in determining spatial autocorrelation.  It looks at the deviation from the mean of every observation, in relation to every other observation, all weighted by a spatial matrix, which takes into account the neighbors file that I mentioned above.  This gives you a global Moran value to determine what type of correlation your total dataset is exhibiting.

To look for local patterns, you can calculate the local Moran's I for each geographic unit in your data.  This will help you easily identify hotspots or coldspots, ie which locations are displaying higher or lower than expected values in your data.
