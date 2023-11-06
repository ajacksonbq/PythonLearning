#Bonus Table

#Create a Dictionary

employees = [
    {"name": "michael", "salary": 32_000, "education": 2, "loyalty": 1},
    {"name": "joe", "salary": 75_000, "education": 4, "loyalty": 3},
    {"name": "laura", "salary": 120_000, "education": 6, "loyalty": 5},
    {"name": "john", "salary": 180_000, "education": 8, "loyalty": 7}
]

#Define Salary

salaries = {employee['name']: employee['salary'] for employee in employees}
#print(salaries)

#Define Education

education = {employee['name']: employee['education'] for employee in employees}
#print(education)

#Define Loyalty (Years with the Company)

loyalty = {employee['name']: employee['loyalty'] for employee in employees}
#print(loyalty)

#Define Bonus

bonuses = {}

for employee in employees:
    bonus = employee['salary'] * (employee['education'] / 100) + (employee['loyalty'] / 100)
    bonuses[employee['name']] = bonus

for name, bonus in bonuses.items():
    print(f"{name.capitalize()}'s bonus: {bonus}")

#for employee in employees:
#    print(f"{employee['name'].capitalize()}'s salary: {employee['salary']:,}")