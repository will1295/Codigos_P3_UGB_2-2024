#Lo que se va a intentar ejecutar
while True:
    try:
        num1 = int(input("Escribe un número: "))
        num2 = int(input("Escribe otro número: "))
        print(num1*num2)
        break
    #Lo que se ejecuta en caso de que genera una excepcion
    except:
        print("Error porfavor ingrese un número válido")

