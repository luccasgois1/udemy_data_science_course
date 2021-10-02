import pandas as pd
from matplotlib import pyplot as plt


def scatter_plot(x,y):
    plt.plot(df[x],df[y],'.',ms=10)
    plt.xlabel('Stock price - ' + x)
    plt.ylabel('Stock price - ' + y)
    plt.title('{d[0]} X {d[1]}'.format(d=[x,y]))
    plt.show()


path_file = 'dataset.csv'
df = pd.read_csv(path_file,sep='\t',decimal=',',parse_dates=['Date'],dayfirst=True)

scatter_plot(df.columns[1], df.columns[2])
scatter_plot(df.columns[1], df.columns[3])

