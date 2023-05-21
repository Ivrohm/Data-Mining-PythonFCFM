import pandas as pd

df = pd.read_csv('columnas_tratar.csv')

print(df.columns)
print(df['Platform'].unique())
print(df['Publisher'].unique())
print(df.describe())

datos =['NA_Sales','EU_Sales','JP_Sales','Global_Sales', 'Other_Sales','Critic_Score']
print("\nCorrelacion")#correlacion
print(df[datos].corr())#correlacion
print("\nMediana")#media
print(df[datos].median())#media
print("\nKurtosis")#kurtosis
print(df[datos].kurtosis())#kurtosis

print(df[datos].sum())
