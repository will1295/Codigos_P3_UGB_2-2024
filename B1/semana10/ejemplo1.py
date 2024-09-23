import numpy as np


array1d = np.array([1,2,3,4,5,6,7,8,9])
print(array1d)

array2d = np.array([[1,2,3],[4,5,6]])
print(array2d)

array3d = np.array([[[1,2,3,4],
                     [5,6,7,8],
                     [9,10,11,12]],
                     [[13,14,15,15],
                      [16,17,18,16],
                      [19,20,21,20]]])

print(array3d)


arreglo = np.arange(1,25,2)
print(arreglo)
print(arreglo.max())
print(arreglo.argmax())
print(arreglo.min())
print(arreglo.argmin())

arreglo2 = np.random.randint(0,50,10)
print(arreglo2)
print(arreglo2.max())
print(arreglo.argmax())
print(arreglo2.min())
print(arreglo.argmin())
