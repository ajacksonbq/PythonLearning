import math

def pythagorean_theorem(a, b):
    c = math.sqrt(a**2 + b**2)
    return c

# Using the function
hypotenuse_length = pythagorean_theorem(3, 4)
print(hypotenuse_length)  # Output: 5.0