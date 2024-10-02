import matplotlib.pyplot as plt
from collections import Counter

est = ["Maria","Juan","Dennys","Luis","Alberto"]
lugar = ["San Miguel","San Miguel"
         ,"Usulután","Morazán","La Unión"]
frecuencia = Counter(lugar)
lugares = list(frecuencia.keys())
cant = list(frecuencia.values())
plt.bar(lugares,cant)
plt.title("Lugar de procedencia de los estudiantes")
plt.xlabel("Lugar de procedencia")
plt.ylabel("Cantidad de estudiantes")
plt.show()
