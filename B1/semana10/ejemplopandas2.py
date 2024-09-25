import pandas as pd

archivo = "canciones.csv"
df = pd.read_csv(archivo)
print(df)

reg = df[df["artist(s)_name"]=="Nicki Minaj"]
print(reg.head(10))