#exercises = []

#while True:
#    user_input = input("New Exercise? (y/n): ")
#    if user_input.upper() == "Y":
#        exercise = input("Enter Name of Exercise: ")
#        exercises.append(exercise)
#        print(exercises)
#    elif user_input.upper() == "N":
#        print("Your Exercises: " + str(exercises))
#        break
#    else:
#        print("Error")

#Add Sets/Reps Failure Reps
#Optionally add Weight

#--------------------

exercises = {}

while True:
    user_input = input("Do you want to add an exercise? (y/n): ")
    if user_input.lower() == 'y':
        exercise = input("Enter the exercise: ")
        sets = input("Enter the number of sets: ")
        reps = input("Enter the number of reps (or 'F' for failure): ")
        add_weight = input("Do you want to add weight? (y/n): ")
        if add_weight.lower() == 'y':
            weight = input("Enter the weight: ")
            exercises[exercise] = {'sets': sets, 'reps': reps, 'weight': weight}
        else:
            exercises[exercise] = {'sets': sets, 'reps': reps}
    elif user_input.lower() == 'n':
        print(exercises)
        print("Done")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

print("Exercises: ", exercises)
