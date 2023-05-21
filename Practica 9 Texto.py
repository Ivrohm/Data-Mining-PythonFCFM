import pandas as pd

import matplotlib.pyplot as plt

from wordcloud import WordCloud

from scipy import stats

from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as line


df = pd.read_csv('columnas_tratar.csv')


texto = ' '.join(df['Developer'].astype(str).tolist())

n_palabras = pd.Series(texto.lower().split()).value_counts()


wordcloud = WordCloud(
    background_color="white", min_font_size=5
).generate_from_frequencies(n_palabras)

n_palabras = pd.Series(texto.lower().split()).value_counts().reset_index()
n_palabras.columns = ['Palabra', 'Repeticiones']


n_palabras.to_csv("Total de palabras repetidas.csv", index=False)

plt.close()


plt.figure(figsize=(5, 5), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

plt.show()
print(n_palabras)


