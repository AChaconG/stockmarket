import yfinance as yf
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

tsla = yf.Ticker("TSLA")
print(tsla)
hist = tsla.history()
#print(hist)
high = list(hist['High'])
low = list(hist['Low'])
date =list(hist.index.date)

plt.close('all')
sns.set()
ax = plt.subplot()
plt.bar(date, high)
plt.bar(date, low)
ax.set_yticks([0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
ax.set_xticklabels(date, rotation = 30)
plt.show()