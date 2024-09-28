import pandas as pd
from statistics import mean

df = pd.read_csv("steam.csv")
def esprev(rat):
    if rat == "Very Positive":
        calif = "Muy positiva"
        return calif

df['Review_type'] = df['Review_type'].apply(esprev)
subsel = df[['Name'
             ,'Price'
             ,'Review_type'
             ]][(df['Price']<=50.0)&(df['Price']!=0.0)]
print(subsel.head(20))

def pprecios(subsel):
    return subsel['Price'].mean()

print(pprecios(subsel))



