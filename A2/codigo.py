#print("Hola Mundo")

"""
Tipos de datos en Python
....
"""
variable1 = "Esto es un valor" #String
variable2 = 20 #Entero
varable3 = 12.4 #Float
variable4 = True #Boolean
variable5 = [23,5,8,12,4,8,9] #Lista

"""
Operadores aritmeticos + - * /, // % **
"""
num1 = 20
num2 = 10.23
print(num1/num2)
print(num1//num2)
print(21%10)

"""
Operadores lógicos and or not

AND

TRUE - TRUE = TRUE
TRUE - FALSE = FALSE
FALSE - TRUE = FALSE
FALSE - FALSE = FALSE
"""
print(True and True)
print(True and False)
print(False and True)
print(False and False)

"""
OR
TRUE - TRUE = TRUE
TRUE - FALSE = TRUE
FALSE - TRUE = TRUE
FALSE - FALSE = FALSE
"""
print("----------------------")
print(True or True)
print(True or False)
print(False or True)
print(False or False)

#NOT
print("-------------------")
print(not True)
print(not False)

"""
Operadores de comparacion <> <= => == !=
"""
print("--------------------")
print(9<10)
print(10<10)

print("Hola Mundo"!="Hola  Mundo")
print("10")

print("Ingrese la altura")
altura = float(input())
print("Ingrese la base")
base = float(input())
print("El resultado es: ",(base*altura)/2)

print("Ingrese la temperatura en C°")
tc = float(input())

tf = (1.8*tc+32)
print(tf)




