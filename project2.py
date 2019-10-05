# James Morrissey
# Data used located at https://www.kaggle.com/AnalyzeBoston/crimes-in-boston#crime.csv

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('classic')



crime = pd.read_csv('crime.csv', encoding='unicode_escape')
crime = crime.set_index('INCIDENT_NUMBER')
crime['OCCURRED_ON_DATE'] = pd.to_datetime(crime.OCCURRED_ON_DATE)
crime['SHOOTING'] = crime['SHOOTING'].replace('Y', 1)
crime['SHOOTING'].fillna(0, inplace=True)

# Amount of crimes in each year
crime_2015 = len(crime[crime.YEAR == 2015])
crime_2016 = len(crime[crime.YEAR == 2016])
crime_2017 = len(crime[crime.YEAR == 2017])
crime_2018 = len(crime[crime.YEAR == 2018])

# Most common types of crimes
crime.OFFENSE_DESCRIPTION.value_counts().head()
# Crime stats by area
crime_area = crime.groupby('DISTRICT')['OFFENSE_DESCRIPTION'].value_counts()
# Crime stats by month for 2018
filtered_crime = crime.query('YEAR == 2018')
by_month = filtered_crime.MONTH.value_counts().sort_index()

# Monthly Shooting Numbers for each Year
shootings = crime[['OCCURRED_ON_DATE', 'SHOOTING']]
shootings.set_index('OCCURRED_ON_DATE',inplace=True)
monthly_shooting = shootings.groupby(pd.Grouper(freq='M'))['SHOOTING'].sum()
shootings2016 = monthly_shooting[monthly_shooting.index.year == 2016]
shootings2017 = monthly_shooting[monthly_shooting.index.year == 2017]
shootings2018 = monthly_shooting[monthly_shooting.index.year == 2018]

shootings2016.plot()
plt.title('Boston Shootings per Month in 2016')
plt.tight_layout(rect=(0.01, 0, 1, 1))
plt.xlabel('Month of Shooting')
plt.ylabel('Number of Shootings')
plt.show()


# Crime indexed by month. Index is a DatetimeIndex
crime.set_index('OCCURRED_ON_DATE', inplace=True)
crime.index = crime.index.to_period('M')
crime.sort_index(ascending=False, inplace=True)
crime.index = crime.index.to_timestamp()




