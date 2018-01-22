#exec(open("C:\\Users\KUBA\Dysk Google\python\datascience\energy.py").read())

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
#%matplotlib inline

columnnames = ['date', 'hour', 'energy']

df1 =  pd.read_csv('GEN_WIATR_20180101_20180120_20180120163514.csv', sep = ';', header = None, names = columnnames, decimal = ',', encoding = 'utf_8')

df2 = pd.read_csv('GEN_WIATR_20171201_20171231_20180104110523.csv', sep = ';', names = columnnames, skiprows = 1,  decimal = ',', encoding = 'utf_8')

df3 = pd.read_csv('GEN_WIATR_20171201_20171231_20180104110523.csv', sep = ';', names = columnnames, skiprows = 1,  decimal = ',', encoding = 'utf_8')

#połączenie 3 plików csv do jednego, uzystaknie okresu od listopada 2017 do 20-01-2018
df3 = df3.append(df2, ignore_index = True)
df3 = df3.append(df1, ignore_index = True)
#proba stworzenia opisu na os x opisu dat, nieudane

#df1.set_index('date',inplace=True)
'''
fig, ax = plt.subplots(figsize=(15,7))
df1.plot(ax=ax)

ax.xaxis.set_major_locator(mdates.WeekdayLocator())

ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))

'''
average = df3['energy'].mean()

plt.plot(df3['energy'], color = 'black', label = 'Produkcja')
plt.title('Generacja energii z źródeł wiatrowych')
plt.xlabel('Date')
plt.ylabel('Production [MW]')
plt.xlim(0)
plt.grid(True)

print(average)
plt.show()



