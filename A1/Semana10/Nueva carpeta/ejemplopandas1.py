import pandas as pd

archivo = "canciones.csv"
df = pd.read_csv(archivo)
#print(df)

#filtro = df[df['artist(s)_name']=="Taylor Swift"]
filtro = df[df['artist(s)_name'].str.contains("Ozuna")]
print(filtro.head(10))