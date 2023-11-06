roster = {
    "Alice": 9,
    "Bob": 10,
    "Charlie": 8,
    "David": 9,
    "Emily": 10
}

print()
print("Roster: ")
print(roster)
print()

roster.update({"Alice": 10})
print(roster)
print()

roster.pop("Bob")
print(roster)
print()

roster["Emily"] += 1
print(roster)
print()

roster.update({"Fiona": 8})
print(roster)
print()

roster["Charlie"] += 1
print(roster)
print()

# Initial roster of kids in the class
#class_roster = {
#    "Alice": 9,
#    "Bob": 10,
#    "Charlie": 8,
#    "David": 9,
#    "Emily": 10
#}

# Print initial roster
#print("Initial Roster:")
#print(class_roster)
#print()

# Scenario 1: Grade Update - Alice's grade changed from 9th to 10th.
#class_roster["Alice"] = 10

# Scenario 2: Course Drop - Bob dropped the course.
#del class_roster["Bob"]

# Scenario 3: Grade Update - Emily's grade changed from 10th to 11th.
#class_roster["Emily"] = 11

# Scenario 4: New Student - Fiona, who is in 8th grade, joined the class.
#class_roster["Fiona"] = 8

# Scenario 5: Grade Update - Charlie's grade changed from 8th to 9th.
#class_roster["Charlie"] = 9

# Print updated roster
#print("Updated Roster:")
#print(class_roster)
