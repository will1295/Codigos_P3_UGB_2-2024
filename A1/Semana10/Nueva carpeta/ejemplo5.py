import numpy as np

array1d = np.array([1,2,3,4])
array2d = np.array([[5,6,7,8],
                    [9,10,11,12]])

array3d = np.array([[[1,2,3,4],
                     [5,6,7,8],
                     [9,10,11,12]],
                     [[13,14,15,16],
                      [17,18,19,20],
                      [21,22,23,24]]])

print(array1d[3])
              #x,y
print(array2d[(0,2)])
              #x,y,z
print(array3d[(1,1,2)])

print(array1d[0:2])
print(array2d[0:1,0:2])
print(array3d[0:1,0:1,0:2])