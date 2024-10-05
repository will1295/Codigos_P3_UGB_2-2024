import matplotlib.pyplot as plt

opciones = ["San Miguel","Usulután","Morazán"
            ,"La Unión"]
frecuencia = [10,2,5,4]
colores = ["red","blue","yellow","green"]
plt.bar(opciones,frecuencia
        ,color=colores,width=0.5,linewidth=3
        ,edgecolor="black")
plt.show()
