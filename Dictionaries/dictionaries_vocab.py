my_dict = {"apple": 3, "banana": 1, "cherry": 2}

key = "apple"
value = my_dict[key]
#print(my_dict.get("apple"))
#print(value)

#Dictionary: A collection of key-value pairs.
#Key: A unique identifier for a value in the dictionary.
#Value: The data stored in the dictionary for a given key.

value = my_dict["banana"]
#print(value)

#get(): A method to retrieve a value for a given key, with an option to provide a default value if the key is not found.
#print(my_dict.get("apple")) #prints 3

#print(my_dict.get("orange", 0)) #prints 0
#print(my_dict.get("orange")) #prints none
#print(my_dict.get("cherry"))

#Asign variable, 'call' dictionary variable ie. 'my_dict', 

#key is variable
#value goes into the dictionary, finds 'key' which is apple, and prints its number '3'

#Items: The key-value pairs in the dictionary.
items = my_dict.items()  # dict_items([('apple', 3), ('banana', 1), ('cherry', 2)])
#print(items) ^

#value = my_dict.setdefault("apple", 0)  # value is 3, dict remains unchanged
#value = my_dict.setdefault("orange", 0)  # value is 0, and 'orange' is added to the dictionary with value 0
#print(value)

keys = my_dict.keys()
#print(keys) (["apple", "banana", "cherry"])

values = my_dict.values()
#print(values) ([3, 1, 2])

#update(): A method to update the dictionary with elements from another dictionary or from an iterable of key-value pairs.
my_dict.update({"banana": 4, "orange": 1})
print(my_dict)

#value = my_dict.pop("apple")
#print(my_dict)

#item = my_dict.popitem() #??
#print(item)

#clear(): A method to remove all items from the dictionary.
#clear = my_dict.clear()
#print(clear)

#copy_dict = my_dict.copy()  # copy_dict is a new dictionary with the same items as my_dict
#print(copy_dict)

#size = len(my_dict)
#print(size)

#exists = "apple" in my_dict # True
#exists = "orange" in my_dict # False
#print(exists)

#defaultdict: A subclass of the built-in dict class from the collections module. It overrides one method to provide a default value for a nonexistent key.
#from collections import defaultdict
#d = defaultdict(int)
#d['key'] += 1  # d['key'] is automatically initialized to 0, then incremented to 1
#print(d)

#OrderedDict: A subclass of the built-in dict class from the collections module that maintains the order in which items are inserted.
#from collections import OrderedDict
#od = OrderedDict()
#od['apple'] = 3
#od['banana'] = 1
#od['cherry'] = 2
# Items will be returned in the order they were added
#print(od)

#Dictionary Comprehension: A concise way to create dictionaries.
squares = {x: x*x for x in range(6)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares)