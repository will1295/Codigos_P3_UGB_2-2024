#listas []
        #    0       1     2      3
lista1 = ["Maria","Juan","Ana","Karla"]
        #   -4      -3    -2     -1

#Index
print(lista1.index("Karla"))
#print(lista1.index("Pedro"))

#Insertar valores
lista1.append("Carlos")
print(lista1)

lista1.insert(3,"Mauricio")
print(lista1)

#Modificar
print(lista1[4])
print(lista1[5])
print(lista1[-1])
lista1[1]="Juan Perez"
print(lista1)

#Eliminar
lista1.remove("Carlos")
lista1.pop(2)
print(lista1)

#Ordenar
#lista1.sort()
lista1.sort(reverse=True)
print(lista1)

#Longitud
print(len(lista1))

#tuplas ()
paises = ("Guatemala","El Salvador","Honduras","Nicaragua")
print(paises[0])
#paises[1]="E.S."
#paises.append("Costa Rica")

#conjunto {}

cnums = {3,8,9,12,6,2,9}
print(cnums)
cdatos = {"SM","US","MO","LU"}
print(cdatos)
cdatos.add("SV")
print(cdatos)
cdatos.remove("SM")
print(cdatos)

#Diccionario

est={"estudiante1":"Maria","estudiante2":"Juan","estudiante3":"Luis"}
print(est)
print(est["estudiante1"])

print(est.keys())
print(est.values())
print(est.items())

print(est.get("estudiante4"))
print(est.get("estudiante1"))
est.setdefault("estudiante5","Saul")
print(est)

datos_di={"verduras":["tomates","cebollas","zanahorias"],
          "frutas":["manzanas","guineros","melones"]}
print(datos_di)
print(datos_di["verduras"])

datos_est={"Roberto":{
    "carnet":"SMS12351",
    "carrera":"Arquitectura",
    "sede":"San Miguel",
    "materias":["Topografia","Estudio de suelos"]
},
"Veronica":{
    "carnet":"SMS112351",
    "carrera":"Enfermeria",
    "sede":"Usulutan",
    "materias":["Salud publica","Asistencia medica"]
}}

print(datos_est["Roberto"]["carnet"])
print(f"Veronica está estudiando: {datos_est['Veronica']["carrera"]}")