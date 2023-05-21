import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('columnas_tratar.csv')

#NA_Sales', 'EU_Sales', 'JP_Sales', 'Global_Sales', 'Name', 'Platform',
  #     'Year_of_Release', 'Genre', 'Publisher', 'Developer', 'Critic_Score'], 
   #   dtype='object')


ax = df.boxplot(column="NA_Sales", by="Year_of_Release",figsize=(8, 10))
plt.show()

ax2 = df.boxplot(column="Year_of_Release", by="Publisher",figsize=(8, 10))
plt.show()

