import numpy as np

arreglo = np.array([10,20,30,40])


print(arreglo[0])

arreglo2 = np.array([[1,2,3],
                     [4,5,6]])
print(arreglo2[0,1])
                #     0  1  2  3  4  5  6  7  8  9
arreglo3 = np.array([10,20,30,40,50,60,70,80,90,100])
print(arreglo3[3:8])
print(arreglo3[:4])
print(arreglo3[::2])


array2d = np.array([[1,2,3],[4,5,6]])
print(array2d[0:2,1:3])