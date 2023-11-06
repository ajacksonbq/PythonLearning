# Define a list of dictionaries, where each dictionary represents an employee
employees = [
    {"name": "John Doe", "base_salary": 50000, "years_experience": 3, "performance_score": 5, "attendance_rate": 98},
    {"name": "Jane Doe", "base_salary": 60000, "years_experience": 6, "performance_score": 3, "attendance_rate": 92},
    {"name": "Alice", "base_salary": 55000, "years_experience": 7, "performance_score": 4, "attendance_rate": 99},
    {"name": "Bob", "base_salary": 48000, "years_experience": 2, "performance_score": 5, "attendance_rate": 96},
]

def calculate_bonus(employee):
    bonus = 0
    
    # Check years of experience
    if employee["years_experience"] > 5:
        bonus += 0.10 * employee["base_salary"]
        
    # Check performance score
    if employee["performance_score"] >= 4:
        bonus += 0.15 * employee["base_salary"]
        
    # Check attendance rate
    if employee["attendance_rate"] >= 95:
        bonus += 0.05 * employee["base_salary"]
        
    return bonus

def main():
    for employee in employees:
        bonus = calculate_bonus(employee)
        print(f"{employee['name']} receives a bonus of ${bonus:.2f}")

if __name__ == "__main__":
    main()
