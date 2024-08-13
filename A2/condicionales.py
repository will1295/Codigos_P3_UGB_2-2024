"""
name = input("Hola, dime tu nombre: ")
if name == "Alice":
    print("Hola Alice")


nombre = input("Escribe tu nombre: ")
while True:
    try:
        edad = int(input("¿Cuántos años tienes? "))
        break
    except:
        print("Error, porfavor ingrese solo números!")
        continue

if(edad>=18):
    print(f"Hola {nombre} tienes {edad} años y eres mayor de edad")
elif(edad<18):
     print(f"Hola {nombre} tienes {edad} años y eres menor de edad")
else:
    print("Error")
    

num1 = int(input("Escribe un numero: "))
num2 = int(input("Escribe otro numero: "))
num3 = int(input("Escribe otro numero: "))

#if(num1>num2&num3)
if(num1>num2 and num1>num3):
    print(f"El mayor es {num1}")
elif(num2>num1 and num2>num3):
    print(f"El mayor es {num2}")
elif(num3>num1 and num3>num1):
    print(f"El mayor es {num3}")
else:
    print("Los tres numeros son iguales")

i=0
while i<10:
    print("Hello World")
    i+=1


while True:
    nombre = input("Escribe el usuario adecuado: ")
    if(nombre=="Juan"):
        print("Bievenido Juan")
        break
    else:
        print("Usuario incorrecto!")
        continue

"""

while True:
    numero = int(input("Que numero de tabla de multiplicar quieres? "))
    limite = int(input("Hasta donde quieres que llegue la tabla?"))
    
    for i in range(1, limite + 1):
        print(f"{numero} x {i} = {numero * i }")
    
    #repetir = input ("Quieres repetir el Programa? (Si/No): ").lower()
    #if repetir != "si":
    #       break
    

