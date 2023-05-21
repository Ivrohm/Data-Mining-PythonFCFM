import pandas as pd
from scipy import stats
from scipy.stats import f_oneway

df = pd.read_csv('columnas_tratar.csv')

Ventas_NA= df.NA_Sales[df.Publisher =="Nintendo"]
Ventas_EU = df.EU_Sales[df.Publisher =='Microsoft Game Studios']
Ventas_JP = df.JP_Sales[df.Publisher=='Sony Computer Entertainment']


resultado, p = f_oneway(Ventas_NA, Ventas_EU, Ventas_JP)

print("Prueba de Anova para los valores de la marca Nintendo-Microsoft Game Studios-Sony Computer Entertainment:")
print(p )

if p  < 0.05:

    print("La diferencia es p < 0.05")

else:

    print("La diferencia es p > 0.05")
