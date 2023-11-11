import numpy as np

a = np.array([[1, 2, 3, 4, 5, 6, 7],[8, 9, 10, 11, 12, 13, 14]])

# Get Element [r, c]
a15 = a[1, 5]
print(a15)

# Get Row
arow = a[1, :]
print(arow)

# Get Column
acol = a[:, 2]
print(acol)


fancyarray = a[0, 0:7:2]
print(fancyarray)

a[1, 5] = 20 # Index
print(a)