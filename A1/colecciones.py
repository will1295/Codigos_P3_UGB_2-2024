#Listas
       #   0        1      2       3
lista1=["Carlos","Maria","Pedro","Juan"]
       #  -4        -3     -2      -1

print(lista1[0])
print(lista1[-1])

lista2 = [4,6,"Agua",True,4.5]
print(lista2)

print(lista2.index("Agua"))

lista3 = ["Ingles","Matematica","Lenguaje"]
lista3.append("Ciencias")
print(lista3)
lista3.insert(3,"Sociales")
print(lista3)

lista3[1]="Matematicas"
print(lista3)

lista3.remove("Lenguaje")
print(lista3)

lista3.pop(0)
print(lista3)

lista3.sort(reverse=True)
print(lista3)

#lista2.sort()
#print(lista2)

print(len(lista3))


tupla1 = ("San Miguel","La Union","Usulutan","Morazan")
print(tupla1[1])
#tupla1[1]="San Vicente"
#tupla1.append("San Vicente")

conjunto1 = {4,8,9,10,11,15,15}
print(conjunto1)
#conjunto1[0]=1
conjunto1.add(7)
print(conjunto1)
conjunto1.remove(10)
print(conjunto1)

di = {"persona1":"Maria","persona2":"Julian","persona3":"Luis"}
print(di)
print(di["persona1"])

tupla=("pizza", "nuggets", "burrito","hotdog")
print(tupla[0:3])


Integrantes=["Oscar", "Manases","Ismael","Nelson","JIHJ"]
Directiva=("Presidente", "Vicepresidente", "Secretario", "Sindico")
Carnet= {"Oscar":"SMSS065523", "Ismael":"SMSS076723","Nelson":"SMSS127921"}
print(f"El {Directiva[0]} es {Integrantes[0]}")

print(Carnet.keys())
print(Carnet.values())
print(Carnet.items())
print(Carnet.get("Oscar"))
#print(Carnet.get("Carlos"))
Carnet.setdefault("Carlos","SMSS5458O")
print(Carnet)


print(lista1)
#print(lista1[0])

for i in lista1:
    print(i)


autores = {"Edgar Allan Poe":["Corazon Delator",
                              "El cuervo"],
            "Stephen King":["El resplandor",
                            "Cementerio de animales"]}

print(autores["Edgar Allan Poe"])
print(autores["Stephen King"])


datos = {"Juan":{
    "carnet":"SMSS1390",
    "carrera":"Ing en sistemas",
    "dire":"San Miguel",
    "materias":["Programacion","Ingles","Bases de datos"]
},
"Maria":{
    "carnet":"SMSS943850",
    "carrera":"Medicina",
    "dire":"Morazan"
}}

print(f"Direccion de la estudiante: {datos["Maria"]["dire"]}")