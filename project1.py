# James Morrissey
# computingID: jpm9rk
# data obtained from "https://www.kaggle.com/dgomonov
# /new-york-city-airbnb-open-data/downloads/new-york-city-airbnb-open-data.zip/3"


import numpy as np
import pandas as pd
# from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
plt.style.use('classic')

# put the values into a dataframe
bnb = pd.read_csv('AB_NYC_2019.csv')
# Series containing average price per housing group
group_price = bnb.groupby('neighbourhood_group')['price'].mean().sort_values(ascending=False)
# round housing prices to 2 decimal places
group_price = group_price.apply(lambda x: round(x, 2))


# PLOT THE AVERAGE HOUSING PRICE FOR EACH NEIGHBOURHOOD GROUP
group_price.plot(kind='bar')
plt.tight_layout()
plt.xlabel('Neighbourhood Group')
plt.ylabel('Average Housing Price ($)')
plt.title('Average Housing Price by Neighbourhood Group')
plt.show()

bnb = bnb.set_index('id')
# neighborhoods in the bronx and their prices
bronx_neighbourhoods = list(bnb[bnb.neighbourhood_group == 'Bronx']['neighbourhood'].sort_values().unique())
bronx_prices = bnb[bnb.neighbourhood_group == 'Bronx'][['neighbourhood','price']].groupby('neighbourhood')['price']\
    .mean().apply(lambda x: round(x, 2)).sort_values(ascending=False)
# neighbourhoods in staten island and their prices
staten_island_neighbourhoods = list(bnb[bnb.neighbourhood_group == 'Staten Island']['neighbourhood']
                                    .sort_values().unique())
staten_island_prices = bnb[bnb.neighbourhood_group == 'Staten Island'][['neighbourhood', 'price']]\
    .groupby('neighbourhood')['price'].mean().apply(lambda x: round(x,2)).sort_values(ascending=False)
# queens neighbourhoods and their prices
queens_prices = bnb[bnb.neighbourhood_group == 'Queens'][['neighbourhood', 'price']]\
    .groupby('neighbourhood')['price'].mean().apply(lambda x: round(x,2)).sort_values(ascending=False)
queens_neighbourhoods = list(bnb[bnb.neighbourhood_group == 'Queens']['neighbourhood'].sort_values().unique())
# Brooklyn neighbourhoods and their prices
brooklyn_prices = bnb[bnb.neighbourhood_group == 'Brooklyn'][['neighbourhood', 'price']]\
    .groupby('neighbourhood')['price'].mean().apply(lambda x: round(x,2)).sort_values(ascending=False)
brooklyn_neighbourhoods = list(bnb[bnb.neighbourhood_group == 'Brooklyn']['neighbourhood'].sort_values().unique())
# Manhattan neighbourhoods and their prices
manhattan_prices = bnb[bnb.neighbourhood_group == 'Manhattan'][['neighbourhood', 'price']]\
    .groupby('neighbourhood')['price'].mean().apply(lambda x: round(x,2)).sort_values(ascending=False)
manhattan_neighbourhoods = list(bnb[bnb.neighbourhood_group == 'Manhattan']['neighbourhood'].sort_values().unique())


# PLOT AVERAGE HOUSING PRICE BY NEIGHBOURHOOD GROUP AND ROOM TYPE
price_by_type = bnb.pivot_table('price',index='neighbourhood_group', columns='room_type')
price_by_type.plot()
plt.xlabel('Neighbourhood Group')
plt.ylabel('Average Price ($)')
plt.title('Housing Price by Room Type and Group')
plt.show()

# Despite how expensive it is, Manhattan bnbs still get a ton of reviews (and hence have a lot of customers)
reviews = bnb.pivot_table(index='neighbourhood_group', columns='room_type',
                        aggfunc={'number_of_reviews': sum, 'reviews_per_month': 'mean'})


# Level of availability of rooms in New York
availability = bnb.pivot_table('availability_365',index='neighbourhood_group',columns='room_type',margins='True')\
    .min().min()


# lat_max=bnb.latitude.max()
# lat_min=bnb.latitude.min()
# lon_max=bnb.latitude.max()
# lon_min=bnb.latitude.min()
# price=bnb.price.values
# lon=bnb.longitude
# lat=bnb.latitude
# m = Basemap(projection='cyl', resolution='h', llcrnrlat=lat_min, urcrnrlat=lat_max,
#              llcrnrlon=lon_min, urcrnrlon = lon_max, width = 1E6, height=1.2E6)
# m.drawstates(color='gray')
# m.scatter(lon,lat,latlon=True,c=price,cmap='Reds',alpha=0.5)







