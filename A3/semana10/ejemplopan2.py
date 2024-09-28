import pandas as pd

df = pd.read_csv("steam.csv")

#subsel = df[['Name','Price','Review_type']]
#print(subsel.head(30))

#subsel = df[['Name'
#             ,'Price'
#             ,'Review_type'
#             ]].sort_values(by='Price',ascending=False)
#print(subsel.head(30))

subsel = df[['Name'
             ,'Price'
             ,'Review_type'
             ]][(df['Price']<=50.0)&(df['Price']!=0.0)]
print(subsel.head(20))