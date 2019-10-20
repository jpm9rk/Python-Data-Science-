# James Morrissey
# computingID: jpm9rk
# data obtained from "https://www.kaggle.com/dgomonov
# /new-york-city-airbnb-open-data/downloads/new-york-city-airbnb-open-data.zip/3"




import numpy as np
import pandas as pd
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

# neighborhoods in each neighbourhood group
bronx_neighbourhoods = list(bnb[bnb.neighbourhood_group == 'Bronx']['neighbourhood'].sort_values().unique())
staten_island_neighbourhoods = list(bnb[bnb.neighbourhood_group == 'Staten Island']['neighbourhood']
                                    .sort_values().unique())
queens_neighbourhoods = list(bnb[bnb.neighbourhood_group == 'Queens']['neighbourhood'].sort_values().unique())
brooklyn_neighbourhoods = list(bnb[bnb.neighbourhood_group == 'Brooklyn']['neighbourhood'].sort_values().unique())
manhattan_neighbourhoods = list(bnb[bnb.neighbourhood_group == 'Manhattan']['neighbourhood'].sort_values().unique())


def neighbourhood_prices(neighbourhood):
    """
    Return a Series containing the avg bnb prices for each neighbourhood in a neighbourhood group
    :param neighbourhood: (str) particular neighbourhood group
    :return: (pd.Series) Series containing the neighbourhood and avg bnb price
    """
    return bnb[bnb.neighbourhood_group == neighbourhood][['neighbourhood','price']].groupby('neighbourhood')['price']\
        .mean().apply(lambda x: round(x, 2)).sort_values(ascending=False)

print('Average bnb neighbourhood prices in the Bronx',neighbourhood_prices('Bronx'))
print('Average bnb neighbourhood prices in Queens',neighbourhood_prices('Queens'))
print('Average bnb neighbourhood prices in Brooklyn',neighbourhood_prices('Bronx'))
print('Average bnb neighbourhood prices in Staten Island',neighbourhood_prices('Staten Island'))
print('Average bnb neighbourhood prices in ',neighbourhood_prices('Manhattan'))

# PLOT AVERAGE HOUSING PRICE BY NEIGHBOURHOOD GROUP AND ROOM TYPE
price_by_type = bnb.pivot_table('price',index='neighbourhood_group', columns='room_type')
price_by_type.plot()
ax1 = plt.gca()
fig1 = plt.gcf()
ax1.legend(fancybox=True,framealpha=1,shadow=True,borderpad=1)
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


lon = bnb.longitude
lat = bnb.latitude
cost = bnb.price
# Low cost Bnb
low = bnb[bnb.price < 1000]
low_cost = low.price
low_lat = low.latitude
low_lon = low.longitude
# High cost Bnb
high = bnb[bnb.price > 1000]
high_cost = high.price
high_lat = high.latitude
high_lon = high.longitude
# Plotting low cost (for now)
plt.scatter(low_lon, low_lat, label=None, c=low_cost, cmap=plt.cm.get_cmap('coolwarm'), linewidth=0, alpha=0.5)
plt.colorbar(label='price ($)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Bnb Prices Under $1000 by Location')
plt.show()



color = {'Manhattan':'red','Brooklyn':'gold',
                                     'Queens':'coral','Bronx': 'skyblue', 'Staten Island':'palegreen'}

for value in color:
    plt.scatter(bnb[bnb.neighbourhood_group == value].longitude,
    bnb[bnb.neighbourhood_group == value].latitude, c=color[value],
    label=value)
plt.title("Location of BNB's in NYC by Neighbourhood Group")
plt.legend()
plt.show()


plt.title('BNB Housing by Neighbourhood Group in NYC')
plt.xlabel('Longitude')
plt.ylabel('Latitude')











