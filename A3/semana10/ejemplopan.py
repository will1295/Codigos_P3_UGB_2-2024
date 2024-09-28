import pandas as pd

df = pd.read_csv("steam.csv")
#print(df)
#Los primeros 5 datos head()
print("Primeros cinco datos")
print(df.head(10))
#Los ultimos 5 tail()
print("Ultimos cinco datos")
print(df.tail(20))