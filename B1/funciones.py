                 #parametro  
def doblar_valor(numero):
    n2 = numero*2
    return n2 #valor de retorno
n=20              #argumento 
print(doblar_valor(n))
        #40

#Keywords
def descripcion(nombre,animal):
    print(f"Mi mascota es un {animal} y se llama {nombre}")

descripcion(animal="hamster",nombre="harry")

#Default
def calcular_area(altura,base=12):
    area = (base*altura)/2
    return area

print(calcular_area(5,8))
