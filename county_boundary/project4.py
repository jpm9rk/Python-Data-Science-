# James Morrissey
# computingID: jpm9rk

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon
import geopandas as gpd
import descartes
from shapely.geometry import Polygon, Point




denver = pd.read_csv('crime.csv')
# determine if there are any missing values in a column, and if so, how many are there
for column in list(denver.columns):
    print('does', column, 'have any missing values?', denver[column].isnull().any())
    if denver[column].isnull().any():
        print('\t there are', np.sum(denver[column].isnull().values), ' missing values in this column')

just_crime = denver.query('IS_CRIME == 1')
just_traffic = denver.query('IS_TRAFFIC == 1')
just_crime=just_crime[just_crime.GEO_LAT > 35]

denver_pic = gpd.read_file('county_boundary.shp')
fig, ax = plt.subplots(figsize=(7, 7))
ax = plt.gca()
geometry = [Point(xy) for xy in zip(just_crime.GEO_LON,just_crime.GEO_LAT)]
crs={'init':'epsg:4326'}
gdf = gpd.GeoDataFrame(just_crime, crs=crs,  geometry=geometry)
denver_pic.plot(ax=ax,color='white',edgecolor='black')
gdf.plot(ax=ax, color='red')
plt.show()
