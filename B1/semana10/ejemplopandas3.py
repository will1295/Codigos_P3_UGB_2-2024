import pandas as pd

archivo = "Hotel.csv"
df = pd.read_csv(archivo)
#print(df)

#print(df.head(10))
#print(df.tail(10))

#reg = df["n_children"]==1
#Condicion que haya un menor de edad
reg = df[df["n_children"]==1]
print(reg.head(10))
#Condicion que haya tres adultos
reg2 = df[df["n_adults"]==3]
print(reg2.head(10))
reg3 = df[(df["n_children"]==1) & (df["n_adults"]==2)]
print(reg3.head())

reg4 = df.groupby("year").size()
ordenasc = reg4.sort_values(ascending=True)
print(ordenasc)

