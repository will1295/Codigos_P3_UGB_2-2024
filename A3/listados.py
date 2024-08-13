#indices    0         1          2
lista = ["lapiz","borrador","sacapunta"]
        #   -3        -2         -1

lista2 = [12,1,5,89,0]
lista3 = ["Maria",12,True]

print(lista.index("lapiz"))
#lista.index("lapicero")

lista2.append(7)
print(lista2)
lista2.insert(2,10)
print(lista2)

indice = 0
for i in lista:
    print(lista[indice])
    indice+=1

lista[1]="corrector"
print(lista)

if(lista[0]=="lapiz"):
    print("Hay un lapiz")

lista3.remove(12)
print(lista3)
lista3.pop(0)
print(lista3)

lista2.sort(reverse=True)
print(lista2)


tupla1 = ("computadora","mouse","teclado","monitor")
print(tupla1[2])

conjunto1 = {3,7,9,1,4,6,0,4,6}
print(conjunto1)
conjunto1.add(20)
print(conjunto1)
conjunto1.remove(7)
print(conjunto1)

my_dict = {"nombre": "william", 
           "apellido":"guandique",
           "edad": 18, 
           "ciudad":"san miguel",
           "estatura": 1.70}

print(f"Mi nombre es: {my_dict['nombre']} {my_dict['apellido']}")


print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

print(my_dict.get("nombre"))
my_dict.setdefault("universidad","ugb")
print(my_dict)
my_dict["universidad"]="universidad gerardo barrios"
print(my_dict)

lista4= ["Maria","Juan","Angel","Pedro","Ana"]
print(lista4[1:4])


compras = {"verduras":["zanahorias","lechuga","tomate"]
           ,"frutas":["manzana","guineos","melon"]}

print("Listado de verduras: ")
for i in compras["verduras"]:
    print(i)

datos = {"Pedro":{
    "Carrera":"Ing en sistemas",
    "Edad":20,
    "Materias":["Programacion","Bases de datos","Ingles"]
},"Juan":{
    "Carrera":"Psicologia",
    "Edad":19,
    "Materias":["Psicologia social","Analisis","Investigacion"]
}
}

print(datos["Juan"]["Carrera"])


rutina = {
    "nombre": "Roberto Carlos Orellana",
    "descripcion": "Rutinal del dia de la manaña",
    "mañana": [
        {"clase": "bañarme", "descripcion": "Preparar la primera clase"},
        {"clase": "siguente clase", "descripcion": "Segunda clase "},
        {"clase": "tercera clase", "descripcion": "clase final para despues almorzar"}
    ]
}

print(rutina["mañana"][1]["descripcion"])



rutina = {
    "Amanecer": {
        "lavarse los dientes", "desayunar", "hacer ejercicio"
    },
    "Atardecer": {
        "jugar", "leer", "cenar"
    }
}

#print(rutina["Amanecer"])
for i in rutina["Amanecer"]:
    print(i)



mi_rutina = {
    "Mañana": {
        "6:00 AM": "Despertar",
        "6:10 AM": "Bañarse",
        "7:00 AM": "Estudiar",
        "9:30 AM": "Desayunar",
    },
    "Tarde": {
        "12:00 PM": "Almuerzo",
        "1:00 PM": "Ir al trabajo",
    },
    "Noche": {
        "7:00 PM": "Cena",
        "8:00 PM": "Leer",
        "10:30 PM": "Dormir"
    }
}

print(mi_rutina["Mañana"]["6:00 AM"])