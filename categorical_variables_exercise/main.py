import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


# Open data
path_file = 'selling_data.csv'
df = pd.read_csv(path_file,index_col=0)

# Create Frequency Distribution Table
df.rename(columns={'n_sell_icecream':'Number of Ice Cream Sold'},inplace=True)

# Create Bar Char
df.plot.bar(rot=0)
# plt.show()

# Create Pie Char
df['Relative frequency (%)'] = (df/df.sum())*100
df.plot.pie(y='Relative frequency (%)',autopct='%1.1f%%')
# plt.show()

# Create Pareto diagram
df.sort_values(by='Number of Ice Cream Sold',inplace=True)
df['Cumulative Number of Ice Cream Sold'] = df.iloc[:,0].cumsum()
ax = df.plot.bar(y='Number of Ice Cream Sold',rot=0)
df.plot.line(y='Cumulative Number of Ice Cream Sold',color='r',ax=ax)
ax.legend(['Cumulative Number of Ice Cream Sold','Number of Ice Cream Sold'])
plt.show()
