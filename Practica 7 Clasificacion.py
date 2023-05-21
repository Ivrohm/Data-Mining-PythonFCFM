import pandas as pd
from scipy import stats
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import statsmodels.formula.api as line


df = pd.read_csv('columnas_tratar.csv')

x= df[[ 'NA_Sales','EU_Sales','JP_Sales','Other_Sales']]
y = df['Global_Sales']

d