fruits = {"apple": 3, "banana": 5, "orange": 2}

quantity = fruits.values() #print(fruits["apple"])
print(quantity)

fruits.update({"banana": 7,}) #fruits["banana"] += 2
print(fruits)

fruits.update({"grape": 4}) 
print(fruits)

fruits.pop("orange")
print(fruits)

strawb = fruits.get("strawberries", 0)
print(strawb)

fruit = ()

for fruit in fruits:
    print(fruits[fruit])

#for fruit, quantity in fruits.items():
#    print(f"{fruit}: {quantity}")


squares = {x: x*x for x in range(6)} #squared_numbers = {x: x*x for x in range(1, 6)}
print(squares)

existence = "apple" in fruits
print(existence)

length = len(fruits)
print(length)