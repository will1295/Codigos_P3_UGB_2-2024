import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({
    "Nombres":["Juan","Maria"
               ,"Pedro","Luis","Ana",
               "Fernanda","Angel","Carlos"],
    "Edad":[20,21,20,20,19,19,18,24]
})

frecuencia = df["Edad"].value_counts()
plt.bar(frecuencia.index,frecuencia.values)
plt.show()