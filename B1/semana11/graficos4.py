import matplotlib.pyplot as plt

comida = ["Hamburguesas","Pizza","Pupusas","Tacos"]
frecuencia = [6,10,4,3]
colores = ["red","yellow","gray","green"]
plt.bar(comida,frecuencia,color=colores)
plt.title("Almuerzo por el día del niño")
plt.xlabel("Opciones de comida")
plt.ylabel("Votos")
plt.show()
