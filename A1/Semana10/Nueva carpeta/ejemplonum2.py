import numpy as np

lista1 = [1,2,3,4]
lista2 = [5,6,7,8]
lista3 = [9,10,11,12]
#
#arra1d = np.array([lista1])
#arra2d = np.array([lista2],[lista3])

array1d = np.array([1,2,3,4])
array2d = np.array([[5,6,7,8],
                    [9,10,11,12]])

array3d = np.array([[[1,2,3,4],
                     [5,6,7,8],
                     [9,10,11,12]],
                     [[13,14,15,16],
                      [17,18,19,20],
                      [21,22,23,24]]])

print(array1d)
print(array2d)
print(array3d)