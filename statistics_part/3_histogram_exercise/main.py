import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


class datasheet:


    def __init__(self, path_file, interval,len_round=True):
        self._path_file = path_file
        self._interval = interval
        self._len_round = len_round
        self.values = None
        self.lim_sup = None
        self.lim_inf = None
        self.freq = []
        self.freq_abs = []
        

    def set_values(self):
        df = pd.read_csv(self._path_file)
        self.values = df.iloc[:,0].values
    

    def set_lim(self):
        vi = self.values.min()
        vf = self.values.max()
        if self._len_round:
            length = np.ceil((vf-vi)/interval)
        else:
            length = (vf-vi)/interval
        list_lim = np.arange(vi,vf+length, length)
        self.lim_inf = list_lim[:-1]
        self.lim_sup = list_lim[1:]

    def set_freq(self):
        for index, i in enumerate(self.lim_inf):
            if index == 0:
                freq = self.values[(self.values<=self.lim_sup[index])&(self.values>=self.lim_inf[index])].shape[0]
                self.freq.append(freq)
            else:
                freq = self.values[(self.values<=self.lim_sup[index])&(self.values>self.lim_inf[index])].shape[0]
                self.freq.append(freq)
        self.freq = np.array(self.freq)

    
    def set_freq_abs(self):
        self.freq_abs = np.around(self.freq / self.freq.sum(),decimals=3)
    

    def create_DataFrame(self):
        self.set_values()
        self.set_lim()
        self.set_freq()
        self.set_freq_abs()

        df = pd.DataFrame({'Value_i':self.lim_inf,'Value_f':self.lim_sup,'Freq':self.freq, 'Freq_Abs':self.freq_abs})

        return df

    
    def plot_histogram(self):
        xlimits = np.unique(np.concatenate((self.lim_inf,self.lim_sup)))
        plt.hist(self.values,bins=xlimits)
        plt.xticks(xlimits)
        plt.grid()
        plt.show()

        
    

path_file = 'dataset.csv'
interval = 10

x = datasheet(path_file, interval)
# x = datasheet(path_file, interval, len_round=False)
df = x.create_DataFrame()
print(df)
x.plot_histogram()