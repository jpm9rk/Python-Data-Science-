# James Morrissey
# computingID: jpm9rk




import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
plt.style.use('classic')
import io
import scipy.stats
import scipy.optimize
import scipy.spatial

stocks = pd.read_csv("all_stocks_5yr.csv")
stocks['date'] = pd.to_datetime(stocks.date)
stocks.dropna(how='all')

CVS = stocks[stocks.Name == 'CVS'].set_index('date')
CVS = CVS['close']
CVS.index = pd.to_datetime(CVS.index)
CVS.asfreq('BM').plot()
