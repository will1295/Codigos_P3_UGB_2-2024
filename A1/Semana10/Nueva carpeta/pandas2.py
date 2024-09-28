import pandas as pd

archivo = "steam.csv"
df = pd.read_csv(archivo)
#print(df)
#filtro = df[['Name','Price','Review_type']]
#print(filtro.head())
filtro = df[['Name'
             ,'Price'
             ,'Review_type'
             ]][(df['Price']<=60.0)
                &(df['Price']!=0.0)].sort_values(
                    by="Name",ascending=True)
print(filtro.head(20))
print(filtro.tail(20))