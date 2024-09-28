import pandas as pd

df = pd.read_csv("juegos.csv")
#print(df)
filtro = df[['Name'
             ,'Price'
             ,'Release_date'
             ]][(df['Price']
                 <=60.0)&(df['Price'])>0]
print(filtro.head(20))