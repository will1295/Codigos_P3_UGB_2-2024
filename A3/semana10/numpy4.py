import numpy as np

        #0,1,2,3,4
lista = [1,2,3,4,5]
arreglo = np.array(lista)

print(arreglo[2])
print(arreglo[1:4])
print(arreglo[:3])
print(arreglo[1:])
       #3x2
print("***************")
matriz2d = np.array([[1,2],
                     [3,4],
                     [5,6]])
print(matriz2d[1:2,1:])
print(matriz2d[1:,1:])
print("***************")

matriz3d = np.array([[[1,2],
                      [3,4]],
                      [[5,6],
                       [7,8]],
                       [[9,10],
                        [11,12]]])
print(matriz3d[1:2,1:,1:])
