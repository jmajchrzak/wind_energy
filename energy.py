#exec(open("C:\\Users\KUBA\Dysk Google\python\datascience\energy.py").read())

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
#%matplotlib inline

columnnames = ['date', 'hour', 'energy']

df1 = pd.read_csv('GEN_WIATR_20180101_20180120_20180120163514.csv', sep = ';', header = None, names = columnnames, decimal = ',', encoding = 'utf_8')

end = pd.datetime(2018, 1, 20)

l_date = pd.date_range('2018-01-01 01:00:00', periods = len(df1), freq = 'H')

df1['date_hour'] = l_date

#df1['day'] = df1['date'] % 20180100

#proba stworzenia opisu na os x opisu dat, nieudane

#df1.set_index('date',inplace=True)
'''
fig, ax = plt.subplots(figsize=(15,7))
df1.plot(ax=ax)

ax.xaxis.set_major_locator(mdates.WeekdayLocator())

ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))

'''

plt.plot( df1['date_hour'], df1['energy'], color = 'black', label = 'Produkcja')
plt.title('Generacja energii z źródeł wiatrowych')
plt.xlabel('Date')
plt.ylabel('Production [MW]')
#plt.xlim(0)
plt.grid(True)


plt.show()
#print(df1)