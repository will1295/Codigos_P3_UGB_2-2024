import matplotlib.pyplot as plt

op = ["Taco bell",
       "Pizza Hut","Wendys","McDonalds"
       ,"China Wok"]
frec = [1,15,11,2,5]
colores = ["purple","blue","yellow","black","red"]
plt.pie(frec,labels=op,autopct="%1.1f%%"
        ,colors=colores)
plt.title("¿Qué comeremos en el convivio?")
plt.xlabel("Opciones")
plt.ylabel("Frecuencia")
plt.show()