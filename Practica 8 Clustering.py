import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import plotly.offline as py

df = pd.read_csv('columnas_tratar.csv')

x = df.iloc[:, [1, 4]].values

_KMeans = KMeans(n_clusters = 3, max_iter = 500, n_init = 1, random_state = 0)
_yMeans = _KMeans.fit_predict(x)

etiquetas = _KMeans.labels_
Centroides = _KMeans.cluster_centers_

plt.figure(1 , figsize = (10 , 8))
plt.scatter(x[_yMeans == 0, 0], x[_yMeans == 0, 1], s = 20, c = 'red', marker = 'o' , label = 'Cluster 1')
plt.scatter(x[_yMeans == 1, 0], x[_yMeans == 1, 1], s = 20, c = 'pink', marker= 's', label = 'Cluster 2')
plt.scatter(x[_yMeans == 2, 0], x[_yMeans == 2, 1], s = 20, c = 'green', marker = 'o', label = 'Cluster 3')
plt.scatter(_KMeans.cluster_centers_[:, 0], _KMeans.cluster_centers_[:, 1], s = 20, c = 'orange', marker = 's',label = 'Centroides')


plt.title('---Venta de videojuegos EUA vs. Ventas Global---')
plt.xlabel('---Ventas de videojuegos en Estados Unidos---')
plt.ylabel('---Ventas de videojuegos en Ventas Global---')
plt.legend()

plt.show()