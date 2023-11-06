my_dict = {
    "Name": "Alex",
    "Age": 18,
    "City": "Springboro",
    "Salary": 100000,
}

#print(my_dict["Salary"])
#del my_dict["Age"]
#print(my_dict)

#my_dict["Job"] = "Accountant"
#my_dict["Age"] = 19

#print(my_dict)

# Iterating through keys
for key in my_dict:
    print(key)

# Iterating through values
for value in my_dict.values():
    print(value)

# Iterating through key-value pairs
for key, value in my_dict.items():
    print(key, value)

# Using get() to safely access keys
age = my_dict.get('age', 'Key not found')
print(age)  # Output: 31

# Using keys(), values(), and items()
print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'job'])
print(my_dict.values())  # Output: dict_values(['Alice', 31, 'Engineer'])
print(my_dict.items())  # Output: dict_items([('name', 'Alice'), ('age', 31), ('job', 'Engineer')])
