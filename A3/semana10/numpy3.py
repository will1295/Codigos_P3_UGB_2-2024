import numpy as np

arreglo = np.array([1,2,3,4,5,6,7,8,9,10])
arreglo2 = np.array([1,2,3,4,5,6])
#2x5
print(arreglo.reshape(2,5))
print("***************")
#2x3, 1x2x3
print(arreglo2.reshape(2,3))
print("***************")
print(arreglo2.reshape(1,2,3))