import numpy as np

#all zeroes matrix

print(np.zeros((2, 5, 5)))
print()
print(np.ones((2, 5, 5)))

print()
print()
print(np.full((2, 5, 5), 1000))
#print(np.full((variable), 10))

rand = np.random.rand(3, 3, 3)
print(rand)

#Random integer values
randominteger = np.random.randint(0, 8, size=(5, 5))
print(randominteger)

# Identity matrix
mat = np.identity(5)
print(mat)

arr = np.array([[1, 2, 3]])
r1 = np.repeat(arr, 3, axis=0)
print(r1)

output = np.ones((5, 5))
print(output)

z = np.zeros((3, 3))
z[1, 1] = 9
print(z)

output[1:-1,1:-1] = z
print(output)