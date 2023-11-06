x = int(input("Enter a Number (x): "))
y = int(input("Enter a Number (y): "))
z = int(input("Enter a Number (z): "))

area = x*y
volume = x*y*z

print("Area: " + str(area))
print("Volume: " + str(volume))

if area > volume:
    print("False")
elif area < volume:
    print("True")
else:
    print("Error")