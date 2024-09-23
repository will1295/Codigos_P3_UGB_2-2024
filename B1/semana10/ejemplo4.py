import numpy as np


arreglo1 = np.array([1,2,3,4,5,6,7,8,9])
arreglo2 = np.array([10,11,12,13,14,15,16,17,18])

print(arreglo1+arreglo2)
print(arreglo1-arreglo2)
print(arreglo1*arreglo2)
print(arreglo1/arreglo2)

matriz1 = np.array([[1,2]
                    ,[3,4]])
matriz2 = np.array([[5,6]
                    ,[7,8]])

print(matriz1+matriz2)
print(matriz1-matriz2)
print(matriz1*matriz2)
print(matriz1/matriz2)


print(np.sqrt(arreglo1))