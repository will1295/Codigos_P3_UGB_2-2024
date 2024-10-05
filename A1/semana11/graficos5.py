import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("steam.csv")

frecuencia = df["Review_type"].value_counts()
plt.pie(frecuencia.values
        ,labels=frecuencia.index,autopct="%1.1f%%")
plt.show()
