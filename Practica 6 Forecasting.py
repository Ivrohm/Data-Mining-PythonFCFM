import pandas as pd
from scipy import stats
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import statsmodels.formula.api as line


df = pd.read_csv('columnas_tratar.csv')

x= df[[ 'NA_Sales','EU_Sales','JP_Sales','Other_Sales']]
y = df['Global_Sales']

model = line.ols(formula = 'Global_Sales ~ NA_Sales',data = df).fit()
prediccion_ventas_global = model.predict(pd.DataFrame(df['NA_Sales']))
pronostico_global = model.predict({'NA_Sales': prediccion_ventas_global})
print(model.params)



ventas_global_pre = model.predict(pd.DataFrame(df['NA_Sales']))

df.plot(kind = 'scatter', x = 'NA_Sales', y = 'Global_Sales')

plt.plot(pd.DataFrame(df['NA_Sales']),ventas_global_pre, color='red',linewidth=2)
plt.plot(pd.DataFrame(df['NA_Sales']),pronostico_global , color='green',linewidth=2)
plt.xticks(rotation=90)
plt.show()

