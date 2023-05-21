import pandas as pd
from scipy import stats
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import statsmodels.formula.api as line


df = pd.read_csv('columnas_tratar.csv')
#df.rename(columns={"Name":"Titulo","Platform" :"Plataforma", "Year_of_Release":"Año_de_lanzamiento", "Genre":"Genero", "Publisher":"Pubicador", "NA_Sales":"NA_Ventas",
 #"Global_Sales":"Ventas_Globales"}, inplace=True)
plataforma = df[[ 'NA_Sales','EU_Sales','JP_Sales','Other_Sales','Year_of_Release']]
print(plataforma)
plt.scatter(plataforma['Year_of_Release'],plataforma['NA_Sales'])
plt.show()