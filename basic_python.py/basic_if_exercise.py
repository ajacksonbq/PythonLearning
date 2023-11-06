#a = int(input("Enter "))

#if a == 1:
#    print("Nice!")
#else:
#    print("Nope!")

#if a != 1:
#    a = a + 1
#    print("Added 1 to a")
#else:
#    print(a)

weight = int(input("weight = "))
unit = input("weight converts to: kg or lb (k/l)")

if unit == "l":
    conversion = weight * 2.2
    print(conversion)
elif unit == "k":
    conversion = weight / 2.2
    print(conversion)
else:
    print("Error")