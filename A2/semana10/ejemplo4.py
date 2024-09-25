import numpy as np

arr1 = np.array([5,13,67,213,8,12,4,22,1])
print(arr1[4])
print(arr1[1:5])
print("********")
print(arr1[1:])
print(arr1[:4])
print("********")

arr2d = np.array([[3,6,10,9,1],
                 [8,13,4,5,2]])
print(arr2d[1,0])
print(arr2d[0:1,1:4])
print("********")
print(arr2d[:2,1:])
print("********")
arr3d = np.array([[[1,2,3,4],
                   [5,6,7,8]],
                   [[9,10,11,12],
                    [13,14,15,16]]])
print(arr3d)
print(arr3d[1,0,1])
print(arr3d[1:2,1:2,1:4])

