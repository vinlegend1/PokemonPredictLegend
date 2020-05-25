import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('Pokemon_Data_with_Total.csv')

m1 = df.loc[(df['Legendary'] == True) & (df['Type 1'] == 'Fire')]
m2 = df.loc[(df['Legendary'] == False) & (df['Type 1'] == 'Fire')]

d1 = df.loc[(df['Legendary'] == True) & (df['Type 1'] == 'Dragon')]
d2 = df.loc[(df['Legendary'] == False) & (df['Type 1'] == 'Dragon')]

z1 = d1['#'].to_list()
z2 = d2['#'].to_list()
y1 = m1['Total'].to_list()
y2 = m2['Total'].to_list()
y3 = d1['Total'].to_list()
y4 = d2['Total'].to_list()
x1 = m1['#'].to_list()
x2 = m2['#'].to_list()

plt.scatter(x1, y1, label = 'Legendaries', c = 'r')
plt.scatter(x2, y2, label = 'Non-Legendaries', c = 'r')

plt.scatter(z1, y3, label = 'Legendaries', c = 'b')
plt.scatter(z2, y4, label = 'Non-Legendaries', c = 'b')
plt.xlabel('Pokedex #')
plt.ylabel('Total Stat Value')
plt.legend()
plt.show()