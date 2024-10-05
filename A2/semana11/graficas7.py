import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("juegos.csv")

fr = df["Review_type"].value_counts()
#plt.bar(fr.index,fr.values)
plt.scatter(fr.index,fr.values)
plt.show()