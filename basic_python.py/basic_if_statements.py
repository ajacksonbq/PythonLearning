temp = int(input("What is the Temperature? "))

warm = str("its a warm day outside")
nice = str("its a nice day outside")
cold = str("its a colder day outside")

if temp > 68:
    print(warm)
elif temp < 68:
    print(cold)
else:
    print(nice)