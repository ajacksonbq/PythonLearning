colleges = {
    "OSU": {"GRate": 94.5, "Enrolled": 32000},
    "WSU": {"GRate": 89.5, "Enrolled": 10200},
    "ASU": {"GRate": 74.5, "Enrolled": 23000},
    "UCLA": {"GRate": 68.9, "Enrolled": 18000}
}

ohio = (colleges["OSU"] ["GRate"])
wright = (colleges["WSU"]["GRate"])
ucla = (colleges["UCLA"]["GRate"])
ohioen = (colleges["OSU"]["Enrolled"])

#print("The Graduation Rate for Ohio State Univeristy is: " + str(ohio) + "%.")
#print("The Graduation Rate for Wright State University is: " + str(wright) + "%.")
#print("The Graduation Rate for UCLA is: " + str(ucla) + "%.")
#print(ohioen)


my_dict = {
    "megan": "female",
    "daniel": "male",
    "alex": "male"
}

#print(f"alex is a {my_dict['alex']}")
my_dict["tyler"] = "male"
my_dict["daniel"] = "female"
print(my_dict)
