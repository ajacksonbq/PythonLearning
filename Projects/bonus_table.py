bonus = float()

while True:
    pay = int(input("What is your pay (yearly)? "))
    education = int(input("How many years of college have you completed? "))
    if education == 0:
        bonus = pay*0.005
        break
    elif education == 1:
        bonus = pay*0.007
        break
    elif education == 2:
        bonus = pay*0.011
        break
    elif education == 3:
        bonus = pay*0.015
        break
    elif education == 4:
        bonus = pay*0.019
        break
    elif education == 5:
        bonus = pay*0.023
        break
    elif education == 6:
        bonus = pay*0.027
        break
    elif education == 7:
        bonus = pay*0.031
        break
    elif education == 8:
        bonus = pay*0.035
        break
    else:
        print("Error, Please Enter a Number")

bonus2 = int()

while True:
        years = float(input("How many years have you been at this company(if less than year, enter months as decimal [3 = .25]? "))
        if years <= 1:
            bonus2 = pay*0.01
            break
        elif years == 2:
            bonus2 = pay*0.012
            break
        elif years == 3:
            bonus2 = pay*0.014
            break
        elif years == 4:
            bonus2 = pay*0.016
            break
        elif years == 5:
            bonus2 = pay*0.018
            break
        elif years == 6:
            bonus2 = pay*0.02
            break
        elif years == 7:
            bonus2 = pay*0.022
            break
        elif years == 8:
            bonus2 = pay*0.024
            break
        elif years == 9:
            bonus2 = pay*0.026
            break
        elif years == 10:
            bonus2 = pay*0.027
            break
        elif years == 11:
            bonus2 = pay*0.029
            break
        elif years == 12:
            bonus2 = pay*0.031
            break
        elif years == 13:
            bonus2 = pay*0.032
            break
        elif years == 14:
            bonus2 = pay*0.033
            break
        elif years == 15:
            bonus2 = pay*0.034
            break
        elif years == 16:
            bonus2 = pay*0.035
            break
        elif years == 17:
            bonus2 = pay*0.036
            break
        elif years == 18:
            bonus2 = pay*0.037
            break
        elif years == 19:
            bonus2 = pay*0.038
            break
        elif years >= 20:
            bonus2 = pay*0.04
            break
        else:
            print("Please Enter a Number ")

total_bonus = bonus + bonus2

print(str(bonus) + " is your estimated bonus check based on education")
print(str(bonus2) + " is your estimated bonus check based on company loyalty")
print(float(total_bonus))