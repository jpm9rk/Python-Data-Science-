# James Morrissey
# computingID: jpm9rk

import numpy as np
import pandas as pd

# change first character of each word to upper case
ser = pd.Series(['how','to', 'play','the','flute'])
ser=ser.apply(lambda x: x.capitalize())

# calculate number of characters in each word in a series
ser = pd.Series(['how','to', 'play','the','flute'])
ser.apply(lambda x: len(x)).values

# compute difference of differences between consecutive numbers of a series
ser = pd.Series([1,3,6,10,15,21,27,35])
ser.diff().to_list()

# convert series of date-strings to a timeseries
ser = pd.Series(['06 February 2013','04-06-2014','20150101','2015/03/09','2016-09-08'])
pd.to_datetime(ser)


# Get day of month, week number, day of year and day of week from series of date strings
ser = pd.Series(['01 Jan 2010', '02-02-2011', '20120303', '2013/04/04', '2014-05-05',
                 '2015-06-06T12:20'])
date = []
week = []
day_num_year = []
day_of_week = []
new_ser = pd.to_datetime(ser)
for value in new_ser:
    date.append(value.month)
    week.append(value.week)
    day_num_year.append(value.dayofyear)
    day_of_week.append(value.dayofweek)
date,week,day_num_year,day_of_week,list(new_ser.dt.day_name().values)


# convert year-month string to dates corresponding to 4th day of the month
ser = pd.Series(['Jan 2010', 'Feb 2011', 'Mar 2012'])
ser=pd.to_datetime(ser)
pd.Series(ser.values + pd.to_timedelta(3,'D'))

# Filter words that contain at least 2 vowels from a series
ser = pd.Series(['Apple', 'Orange', 'Plan', 'Python', 'Money'])


def count_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    i = 0
    for letter in str:
        if letter in vowels:
            i += 1
    if i >= 2:
        return np.nan
    return str


ser.apply(count_vowels).dropna()


# Mean of a series grouped by another series
fruit = pd.Series(np.random.choice(['apple', 'banana', 'carrot'], 10))
weights = pd.Series(np.linspace(1, 10, 10))
df = pd.concat([fruit,weights],axis=1)
df.columns = [['fruit','weight']]
df.groupby(fruit).mean()


