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
    
