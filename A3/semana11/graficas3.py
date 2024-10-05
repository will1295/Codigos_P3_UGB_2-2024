import matplotlib.pyplot as plt

dep = ["San Miguel","Usulután","La Unión","Morazán"]
frec = [11,1,4,1]
colores = ["red","yellow","blue","green"]
plt.bar(dep,frec,color=colores)
plt.title("Lugar de procedencia")
plt.xlabel("Departamento")
plt.ylabel("Frecuencia")
plt.show()