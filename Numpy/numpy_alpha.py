import numpy as np

array1 = np.array([100, 200, 300, 400], dtype='int16')
print(array1)

array2 = np.array([[10, 100, 1000, 10000],[5, 50, 500, 5000],[2, 20, 200, 2000]])
print(array2)
array2dim = array2.ndim
print(array2dim)
print(array2.shape)

print(array2.dtype)

print(array2.itemsize)

print(array2.size)
print(array2.nbytes)