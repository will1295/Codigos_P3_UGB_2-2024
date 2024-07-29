#print("Hola Mundo")

"""
 print("Hola Mundo")
 print("Hola Mundo")
 print("Hola Mundo")
 print("Hola Mundo")
"""

variable1 = "Valor"
variable2 = 20
variable3 = True
variable4 = [10,20,18,2,5]

#Operadores artimeticos (suma,resta,mult,div,divent,residuo)

num1 = 2.5
num2 = 1.2
num3 = 12
#total = num1+num2+num3
print(num1//num2)
print(num1%num2)

#operadores logicos and or not xor

"""
AND

TRUE - TRUE = TRUE
TRUE - FALSE = FALSE
FALSE - TRUE = FALSE
FALSE - FALSE = FALSE

OR

TRUE - TRUE = TRUE
TRUE - FALSE = TRUE
FALSE - TRUE = TRUE
FALSE - FALSE = FALSE

XOR

"""

print(True and True)
print(True and False)
print(False and True)
print(False and False)
print("--------------------")
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print("--------------------")
print(not True)
print(not False)
print("--------------------")
num1 = 10
num2 = 27
xor = num1 ^ num2
print(xor)

#Operadores de comparación <> <= => == =!
# 8==8 "hola"=!" hola"

print(7==7)
print("Hola Mundo"=="Hola  Mundo")

print("Digite la altura del triangulo")
altura = float(input())
print("Digite la base del triangulo")
base = float(input())
print("El area del triangulo es ",(base*altura)/2)