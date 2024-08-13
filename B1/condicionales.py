#if
"""
num=int(input("Digite un numero: "))

if(num%2==0):
    print("El numero es par")
else:
    print("El numero es impar")


num1=int(input("Digita un primer numero: "))
num2=int(input("Digita un segundo numero: "))
num3=int(input("Digita un tercer numero: "))

if(num1>num2):
    print(f"El mayor de los numeros es: {num1}")
elif(num1<num2):
    print(f"El mayor de los numeros es: {num2}")
elif(num1==num2):
    print(f"Los numeros son iguales")
else:
    print("No evaluable")
"""

num1=int(input("Digita un primer numero: "))
num2=int(input("Digita un segundo numero: "))
num3=int(input("Digita un tercer numero: "))

if(num1 > num2 and num1 > num3):
    print(f"El numero mayor es: {num1}")
elif num1==num2 or num2==num3 or num1==num3:
    if(num1==num2):
        print(f"{num1} y {num2} son iguales")
    elif(num3==num2):
        print(f"{num3} y {num2} son iguales")
    elif(num3==num1):
        print(f"{num3} y {num1} son iguales")
elif(num1 == num2 and num1 == num3):
    print("Los numeros son iguales.")
elif(num2 > num1 and num2 > num3): 
    print(f"El numero mayor es: {num2}")
elif(num3 > num1 and num3 > num2): 
    print(f"El numero mayor es: {num3}")
else:
    print("no sabo")
