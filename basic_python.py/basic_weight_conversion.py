korl = input("(K)g or (L)bs (Input): ").strip().lower()
weight = float(input("Enter Your Weight: "))

if korl == "k":
    lbs = weight * 2.20462
    print(f"{lbs:.2f} is your weight in lbs")
elif korl == "l":
    kg = weight / 2.20462
    print(f"{kg:.2f} is your weight in kg")
else:
    print("Error: Please enter 'K' for kilograms or 'L' for pounds.")
