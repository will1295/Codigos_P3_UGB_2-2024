#If
"""
name=input("Escribe tu nombre: ")
edad = int(input("Digita tu edad: "))
if name == "Alice":
    print("Hola Alice")
elif edad>12:
    print("Si eres Alice")
else:
    print("No eres Alice")


numero1 = int(input("Escribe un numero: "))
numero2 = int(input("Escribe otro numero: "))
numero3 = int(input("Escribe otro numero: "))

if(numero1>numero2 and numero1>numero3):
    print(f"El mayor es {numero1}")
elif(numero2>numero1 and numero2>numero3):
    print(f"El mayor es {numero2}")
else:
    print(f"El mayor es {numero3}")


#While
spam = 0
while spam<5:
    print("Hello world")
    spam+=1

while True:
    num1 = int(input("Escribe un numero: "))
    num2 = int(input("Escribe otro numero: "))
    num3 = int(input("Escribe otro numero: "))

    if (num1>num2 and num1>num3):
        print(f"El numero mayor es {num1}")
        medio=0
        menor=0
        if (num2>num3):
            medio=num2
            menor=num3
            print(f"El numero medio es {medio}")
            print(f"El numero menor es {menor}")
            op = input("¿Quieres ejecutar otra vez el programa? (S/N)")
            if(op == "N"):
                break
            else:
                continue
            
        else:
            medio=num3
            menor=num2
            print(f"El numero medio es {medio}")
            print(f"El numero menor es {menor}")
            
    elif (num2>num1 and num2>num3):
        print(f"El numero mayor es {num2}")
        medio=0
        menor=0
        if (num1>num3):
            medio=num1
            menor=num3
            print(f"El numero medio es {medio}")
            print(f"El numero menor es {menor}")
        else:
            medio=num3
            menor=num1
            print(f"El numero medio es {medio}")
            print(f"El numero menor es {menor}")
    else:
        print(f"El numero mayor es {num3}")
        medio=0
        menor=0
        if (num1>num2):
            medio=num1
            menor=num2
            print(f"El numero medio es {medio}")
            print(f"El numero menor es {menor}")
        else:
            medio=num2
            menor=num1
            print(f"El numero medio es {medio}")
            print(f"El numero menor es {menor}")

while True:
    tabla = int(input("Ingrese la tabla que desea imprimir: "))
    num = int(input("Ingrese el número hasta que desea imprimir: "))
    for i in range(1,num+1):
        print(f"{tabla} x {i} = {tabla * i}")
    
    op =input("Quieres seguir ejecutando el programa? (s/n)") 
    if op == "n":
        break


"""

for i in range(7):
    continue

def funcion(*args):
    for i in args:
        print(i)

funcion(2,5,89,4,1,6,9)

def info(nom,*materias):
    n = 1
    print(f"Estudiante: {nom}")
    print("Cursa las materias de: ")
    for m in materias:
        print(f"{n}-{m}")
        n+=1

info("Juan","Programacion","Bases de datos","Redes")


def contar_a(palabras):
    contador = 0
    for palabra in palabras:
        contador += palabra.lower().count("a")
    return contador

palabras = ["Hola", "Maundo", "Esto", "Esa", "UnA", "Ejemplo","Hola"]
print(contar_a(palabras))














