students = {
    "Student1": {"Name": "Jared", "Grade": 10}
}

students["Student2"] = {"Name": "Emily", "Grade": 9}
students["Student3"] = {"Name": "Michael", "Grade": 11}
students["Student4"] = {"Name": "Jessica", "Grade": 10}

print(students)

print(students["Student2"]["Name"])  # Outputs: Emily
print(students["Student3"]["Grade"])  # Outputs: 11

students = {
    "Jared": {"Grade": 10, "Age": 15},
    "Emily": {"Grade": 9, "Age": 14},
    "Michael": {"Grade": 11, "Age": 16},
    "Jessica": {"Grade": 10, "Age": 15}
}

students = {
    "Jared": [10, 15],  # Grade, Age
    "Emily": [9, 14],
    "Michael": [11, 16],
    "Jessica": [10, 15]
}

student_grades = {
    "Jared": 10,
    "Emily": 9,
    "Michael": 11,
    "Jessica": 10
}