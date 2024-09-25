import numpy as np

lista = [1,2,3,4,5,6,7,8,9,0]
arreglo = np.array(lista)
print(arreglo)
#10.... 2x5 5x2
matriz = arreglo.reshape((2,5))
print(matriz)

lista2 = [1,2,3,4,5,6,7,8,9,10,11,12]
arreglo2 = np.array(lista2)
print(arreglo2)
#10.... 2x6,3x4,2x2x3
matriz3d = arreglo2.reshape((2,2,3))
print(matriz3d)