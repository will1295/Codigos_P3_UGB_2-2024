import pandas as pd

df = pd.read_csv("musica.csv")
#print(df)
#print(df.head(10))
#print(df.tail(20))
filtro = df[['track_name'
             ,'artist(s)_name'
             ,'streams'
             ]].sort_values(by='streams'
                            ,ascending=False)
print(filtro.head(10))