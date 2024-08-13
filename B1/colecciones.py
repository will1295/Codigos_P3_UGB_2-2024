#Lista
        #   0       1      2      3     4
lista = ["Maria","Pepe","Juan","Luis","Ana"]
lista[0]="Maria Hernandez"
print(lista)
print(lista[0])
print(lista[1])
print(lista[-1])

#Buscar un valor
print(lista.index("Juan"))
#Agregar un valor
lista.append("Pedro")
print(lista)
lista.insert(2,"Cristian")
print(lista)

#Quitar un valor
lista.remove("Pepe")
print(lista)

#Ordena la lista alfabeticamente
lista.sort()
#lista.sort(reverse=True)
print(lista)

print(len(lista))

#Tupla
        #    0              1          2           3
paises = ("Guatemala","El Salvador","Honduras","Nicaragua")
print(paises[2])
            #i:i-1
print(paises[1:3])
#paises[0]="guatemala"
#paises.remove("Honduras")

numeros = {4,98,2,7,23,8}
print(numeros)


#Diccionario
#Clave:Valor
#Autor:Libro
libros = {"Gabriel Garcia":"100 años de soledad",
          "Homero":"La Iliada","Alfredo Espino":"Jícaras tristes",
          "Edgar Allan Poe":"El escarabajo de oro",
          "William Shakespeare":"Hamlet"}
print(libros["Alfredo Espino"])

listacom = {1:"Tomates",2:"Cebollas",3:"Arroz"}
print(listacom[1])

print(libros.keys())
print(libros.values())
print(libros.items())

print(libros.get("Homero"))
print(libros.get("Stephen King"))
print(libros.setdefault("Franz Kafka","La metamorfosis"))
print(libros)

dic_compras={"verduras":["tomates,cebollas,chile verde,zanahorias"],
             "frutas":["papaya","guineos","sandias"]
             }

print(dic_compras["verduras"])
#Diccionarios anidados
estudiantes = {"Estudiante1":{
    "Nombre":"Pepe",
    "Apellido":"Hernandez",
    "Edad":20,
    "Carrera":"Tecnico de sistemas",
    "Materias":["Programacion","Bases de datos"]
},
    "Estudiante2":{
        "Nombre":"Maria",
        "Apellido":"Gutierrez",
        "Edad":19,
        "Carrera":"Doctorado en Medicina",
        "Materias":["Anatomia","Cardiologia"]
}
}
print(estudiantes["Estudiante1"]["Carrera"])
print(estudiantes["Estudiante2"]["Materias"])


mirutina = {
    "07:00":"Me levanto",
    "8:00":["Desayuno","Veo tv"]
}

rutina_yajaira =  {
            "7:30": "Me despierto",
            "8:00": "Me lavo la cara y sepillo mis dientes",
            "10:40 - 2:20": "Clases",
            "3 - 6": "Chambear",
            "8": "Cena",
            "12": "Mimir"
        }
print(rutina_yajaira) 

Agenda_Fernando_Grinch = {
    "04:00 pm": "Sumergirme en mi propia miseria",
    "04:30 pm": "Contemplar el abismo",
    "05:00 pm": "Solucionar la hambruna mundial sin decírselo a nadie",
    "05:30 pm": "Danza y ejercicio",
    "06:30 pm": "Cena conmigo. Esa no la cancelaré",
    "07:00 pm": "Luchar con el odio que me tengo"
}
print(Agenda_Fernando_Grinch)

mirutinawesly = {"dia1":{
    "7:00":"me levanto",
    "8:00":["me preparo el desayuno", "desayuno lo que prepare"],
    "9:00":"salgo a correr",
    "12:00 PM":["me preparo el almuerzo","me baño", "almuerzo"],
    "2:00 PM":"juego video juegos",
    "4:00 PM":"voy al campo",
    "8:00 PM":"duermo, mentira jaja"
}
}
print(mirutinawesly["dia1"]["4:00 PM"])


mi_rutina_diaria_maurico = {
    "mañana": {
        "6:00 AM": "Despertar",
        "6:30 AM": "Desayuno",
        "7:00 AM": "Tomar el autobús",
        "8:00 AM": "Llegar a la universidad",
        "clases": ["Programación", "Desarrollo web", "Software libre"]
    },
    "tarde": {
        "12:00 PM": "Almuerzo",
        "1:00 PM": "De nuevo a clases",
        "3:00 PM": "Salir de la universidad",
        "5:00 PM": "Llegar a casa"
    },
    "noche": {
        "6:00 PM": "Cenar",
        "7:00 PM": "Tiempo en familia",
        "8:00 PM": "Leer",
        "9:00 PM": "Prepararse para dormir",
        "10:00 PM": "Dormir"
    }
}

print(mi_rutina_diaria_maurico["mañana"]["clases"])


rutina_Alvaro = {
    "despertar": "7:00 AM",
    "desayuno": "9:00 AM",
    "actividad_mañana": "Estudiar",
    "almuerzo": "1:00 PM",
    "actividad_tarde": "Jugar ftbol",
    "cena": "7:00 PM",
    "actividad_noche": "Ver una película",
    "dormir": "10:00 PM"
}

print(rutina_Alvaro)