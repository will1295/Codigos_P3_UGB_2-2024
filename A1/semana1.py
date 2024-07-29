print("Programacion 3")

variable1 = "Valor"
variable2 = 20
variable3 = 12.2
variable4 = True
variable5 = [12,4,79,23,41]

#Operadores aritmeticos + - * / // ** %

num1 = 20
num2 = 3
print(num1//num2)
print(num1%num2)

#Operadores logicos and or not

"""
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
print("-----------------------")
print(not True)
print(not False)

#Operadores de comparacion <> <= => == =!
# 9<10  10<=10

print(9<10)
print(10<=10)
print("Hola Mundo"==" Hola Mundo")

print("Digite el valor de la altura")
altura = float(input())
print("Digite el valor de la altura")
base = float(input())
print("El valor del area es de: ",(base*altura)/2)
