employees = [
    {"name": "Michael", "attendance": 5, "work_ethic": 4, "attitude": 5},
    {"name": "Joe", "attendance": 3, "work_ethic": 5, "attitude": 4},
    {"name": "Laura", "attendance": 4, "work_ethic": 3, "attitude": 5},
    {"name": "John", "attendance": 2, "work_ethic": 4, "attitude": 3},
    # ... add more employees as needed
]

# Define a function to calculate the bonus
def calculate_bonus(attendance, work_ethic, attitude):
    # Assuming max score for each is 5, so max total score is 15
    total_score = attendance + work_ethic + attitude
    max_score = 5 * 3  # max score for each category times number of categories

    # Map the total score to the bonus range of $350 - $1200
    bonus = ((total_score / max_score) * (1200 - 350)) + 350

    return round(bonus, 2)  # round the bonus to two decimal places

# Calculate and display the bonus for each employee
bonuses = {}

for employee in employees:
    bonus = calculate_bonus(employee['attendance'], employee['work_ethic'], employee['attitude'])
    bonuses[employee['name']] = bonus

# Print the bonus table
print("Bonus Table:")
for name, bonus in bonuses.items():
    print(f"{name}: ${bonus}")
