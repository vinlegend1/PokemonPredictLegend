import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv('pokemon_no_mega_data.csv')

EternatusStats = [140, 85, 95, 145, 95, 130]
ZamazentaStats = [92, 130, 145, 80, 145, 128]
CinderaceStats = [80, 116, 75, 65, 75, 119]

stats = df.iloc[:, 5:11]
islegend = df['Legendary']

knn = KNeighborsClassifier(n_neighbors = 2)

knn.fit(stats, islegend)
prediction = knn.predict(np.array(CinderaceStats).reshape(1, -1))
if prediction > 0.5:
	print('Legendary')
else:
	print('not Legendary')