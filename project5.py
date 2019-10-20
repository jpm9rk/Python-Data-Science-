
# James Morrissey



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


nyc = pd.read_csv('AB_NYC_2019.csv')
bnb = pd.read_csv('AB_NYC_2019.csv')
# Series containing average price per housing group
group_price = bnb.groupby('neighbourhood_group')['price'].mean().sort_values(ascending=False)
# round housing prices to 2 decimal places
group_price = group_price.apply(lambda x: round(x, 2))

color = {'Manhattan':'red','Brooklyn':'gold',
                                     'Queens':'coral','Bronx': 'skyblue', 'Staten Island':'palegreen'}


for value in color:
     plt.scatter(bnb[bnb.neighbourhood_group==value].longitude,
     bnb[bnb.neighbourhood_group==value].latitude, c=color[value],
     label=value)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title("BNB's in NYC by Neighbourhood Group")
plt.legend()
plt.show()

bnb.set_index('id',inplace=True)
