import matplotlib.pyplot as plt

x = [0,1,2,3,4,5,6,7,8,9]
y = [2,8,3,2,10,15,5,9,2,1]
plt.plot(x,y,linewidth=3,color="red")
plt.xlabel("Opciones")
plt.ylabel("Frecuencias")
plt.title("Opciones de numeros")
plt.show()
