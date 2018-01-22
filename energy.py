#exec(open("C:\\Users\KUBA\Dysk Google\python\datascience\energy.py").read())
#pse.pl/getcsv/-/export/csv/GEN_WIATR/data_od/20180101/data_do/20180122

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
#%matplotlib inline

columnnames = ['date', 'hour', 'energy']

df1 = pd.read_csv('GEN_WIATR_20180101_20180122_20180122183511.csv', sep = ';', names = columnnames, skiprows = 1, index_col = False, decimal = ',', encoding = 'utf_8')

first_day = df1['date'].iloc[0], df1['hour'].iloc[0]
first_day = str(first_day[0]) + ' ' + str(first_day[1]) + ':00'

df1['date_hour'] = pd.date_range(first_day, periods = len(df1), freq = 'H')

plt.plot( df1['date_hour'], df1['energy'], color = 'black', label = 'Produkcja')
plt.title('Generacja energii z źródeł wiatrowych')
plt.xlabel('Date')
plt.ylabel('Production [MW]')
#plt.xlim(0)
plt.grid(True)

plt.show()


#print(df1)