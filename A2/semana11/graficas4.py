import matplotlib.pyplot as plt

op=["Pizza","Hamburguesas"
    ,"Pollo frito","Pupusas"]
fre=[4,2,3,9]
colores = ["red","blue","yellow","green"]
plt.pie(fre,labels=op
        ,autopct="%1.1f%%",colors=colores)
plt.title("Opciones de almuerzo")
plt.show()