def mifuncion():
    print("Programacion III")
mifuncion()

def par(num):
    residuo = num%2
    if(residuo==0):
        print("Es par")
    else:
        print("Es impar")
par(5)


def areat(base,altura):
    area=(base*altura)/2
    return area

result=areat(20,10)
print(result)
print(areat(20,10))

suma=lambda x:x+3
print(suma(20))

longit = lambda frase:len(frase)
print(longit("Hola Mundo"))


def dist(vel,tiem):
    di=vel*tiem
    metros=lambda d:d/1000
    metros(di)
    return metros

def multi(*args):
    return args

def multi2(**args):
    return args


def lista(mercado,**compras):
    print(compras)

lista["Tomates":"1 Libra","Cebollas":"2"]
"""
lista("Tomates","Cebollas","Sal","Aceite")
lista("Huevos","Leche")
lista()
"""