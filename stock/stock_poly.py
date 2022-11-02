import pandas as pd
import matplotlib.pyplot as plt
import numpy
from scipy import stats

df = pd.read_csv('../csv/AC-30dayHistory-Nov02.csv')

df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %H:%M:%S').dt.strftime('%m-%d')

X = df['Date']
y = df['Close']

plt.scatter(X, y)

plt.show()
