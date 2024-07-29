def doblar_valor(numero):
    n2 = numero*2
    return n2
num = 20
print(doblar_valor(num))


def describir(tipom,nombrem):
    print(f"Mi mascota es un {tipom} y se llama {nombrem}")

describir("Loro","Pancho")
describir("Gato","Michi")
describir("Perro","Firulais")
describir(nombrem="Neptuno",tipom="Pez")


def estudiantes(nombre,apellido,carnet,sede="San Miguel"):
    print(f"Estudiante: {nombre} {apellido} Carnet: {carnet} Sede: {sede}" )

estudiantes("Pepito","Perez","SMSS12345","Usulutan")


def inf(nombre,carnet,carrera,*materias):
    print(f"Informe del estudiante {nombre} de carnet {carnet} de la carrea {carrera}")
    print("Lleva las materias de: ")
    for materia in materias:
        print(f"*{materia}")

inf("Juan Perez","SMSS1234","Ing en sistemas","Programacion","Matematica","Ingles","Electronica","Software Libre")    


def mult():
    total = 3*5
    return total

print("Ingresa un valor que quieras multiplicar 15")
valor = float(input())
print(valor*mult())
