import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({
    'Nombres':["Jimmy","Emerson"
               ,"Alfredo","Javier"
               ,"Daniel","Roberto"
               ,"Luna","Eliseo"
               ,"Derick","Joshua","Brian"
               ,"Ximena","Briseily","William"
               ,"Camila","Berta"],
    'Edades':[27,20,18,19,19,21,19,19,21,19,20,19,
              19,18,20,19]
})

frecuencia = df['Edades'].value_counts()
plt.bar(frecuencia.index.astype(str),frecuencia.values)
plt.title("Edades del grupo A3")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.show()