import numpy as np

lista = [1,2,3,4,5]
arreglo = np.array(lista)
print(type(arreglo))
print(arreglo)

#matriz 3x2
matriz2d = np.array([[1,2],
                     [3,4],
                     [5,6]])
print(matriz2d)
        #x*y*z
#matriz 3x2x2
matriz3d = np.array([[[1,2],
                      [3,4]],
                      [[5,6],
                       [7,8]],
                       [[9,10],
                        [11,12]]])
print(matriz3d)
