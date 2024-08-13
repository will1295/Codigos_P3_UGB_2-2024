#while
"""
i=0
while i<10:
    print(f"Valor de i {i}")
    i+=1
    #i=i+1


valor = int(input("Escribe un numero: "))
i=1
while(i<=valor):
    print(i)
    i+=1

numero = int(input("Digite el número que desea para la tabla de multiplicar: "))
i = 1
while i <= 10:
    print(f"{numero} x {i} = {numero * i}")
    i += 1


while True:
    numero = int(input("Digite el número que desea para la tabla de multiplicar: "))
    i = 1
    while i <= 10:
        print(f"{numero} x {i} = {numero * i}")
        i += 1
    op=input("Seleccione una opcion:\n"+
              "1-Pedir otro numero\n"+
              "2-Salir\n")
    if(op=="1"):
            continue
    elif(op=="2"):
            break
    else:
        print("Opcion incorrecta")
"""
while True:
    usuario = "yo"
    contra = "1234"

    a = input("Escriba su usario: ")
    b = input("Escriba su contraseña: ")

    if(a == usuario and b == contra):
        print("Bievenido")
        break
    else:
        print("usuario o contraseña incorrecta")
        continue