"""
name=input("Digita tu nombre: ")
if(name == "Alice"):
    print("Hola Alice")
elif(name == "Angela"):
    print("Hola Angela")
else:
    print("No eres Alice")


try:
    num1 = int(input("Escribe un numero: "))
except:
    print("Dato incorrecto")

num2 = int(input("Escribe otro numero: "))
num3 = int(input("Escribe otro numero: "))

if(num1==num2 or num2==num3 or num1==num3):
    print(f"Hay numeros repetidos")
elif(num1>num2 and num1>num3):
    print(f"El numero mayor es: {num1}")
elif(num2>num1 and num2>num3):
    print(f"El numero mayor es: {num2}")
elif(num3>num1 and num3>num2):
    print(f"El numero mayor es: {num3}")
else:
    print(f"Los tres numeros son iguales")


contador = 0
while(contador<10):
    print("Hola Mundo")
    contador+=1

while True:
    try:
        num1 = int(input("Escribe un numero: "))
    except:
        print("Dato incorrecto")
    num2 = int(input("Escribe otro numero: "))
    num3 = int(input("Escribe otro numero: "))
    if(num1==num2 or num2==num3 or num1==num3):
        print(f"Hay numeros repetidos")
        op=input("¿Desea ejecutar el programa de nuevo? (S/N)")
        if(op=="N"):
            break
        else:
            continue
    elif(num1>num2 and num1>num3):
        print(f"El numero mayor es: {num1}")
    elif(num2>num1 and num2>num3):
        print(f"El numero mayor es: {num2}")
    elif(num3>num1 and num3>num2):
        print(f"El numero mayor es: {num3}")
    else:
        print(f"Los tres numeros son iguales")
"""


for i in range(5):
    print("Bucle for")


def datos(nomb,*materias):
    num=1
    print(f"Nombre del estudiante: {nomb}")
    print("Materias que cursa: ")
    for m in materias:
        print(f"{num}-{m}")
        num+=1

datos("Juan","Programacion","Bases de datos","Redes")
