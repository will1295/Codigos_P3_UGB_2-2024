import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("steam.csv")
cantidad = df['Review_type'].value_counts()
#cantidad.plot()
colores = ["blue","yellow",
           "green","orange",
           "red","gray","purple","black"]
cantidad.plot(kind="bar",color=colores)
#cantidad.plot(kind="pie")
plt.title("Reviews")
plt.xlabel("Tipo de review")
plt.ylabel("Cantidad")
#plt.axis('equal')
plt.show()