employees = {
    "mike": {"salary": 15_000, "ed": 0, "loyalty": 0},
    "alex": {"salary": 65_000, "ed": 2, "loyalty": 2},
    "jess": {"salary": 100_000, "ed": 4, "loyalty": 4},
    "trey": {"salary": 170_000, "ed": 6, "loyalty": 6},
    "nate": {"salary": 240_000, "ed": 8, "loyalty": 8}
}

#mike_salary = employees["mike"]["salary"]
#mike_education = employees["mike"]["ed"]
#mike_loyalty = employees["mike"]["loyalty"]



for name, data in employees.items():
    salary = data["salary"]
    education = data["ed"]
    loyalty = data["loyalty"]
    
    bonus = salary * (education / 100) * (loyalty / 100)
    print(f"{name.capitalize()}'s bonus: ${bonus:.2f}")