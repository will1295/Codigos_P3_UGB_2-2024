import matplotlib.pyplot as plt

dep = ["San Miguel","Morazán","La Unión","Usulután"]
frec = [18,2,3,3]
colores = ["purple","blue","yellow","black"]
plt.bar(dep,frec,color=colores)
plt.title("Lugares de procedencia")
plt.xlabel("Departamentos")
plt.ylabel("Frecuencia")
plt.show()