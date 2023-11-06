hours = float(input("Enter Hours: "))
pay = float(input("Enter Hourly Pay: "))
tax_rate = float(input("Enter Tax Percentage: "))
tax = float(tax_rate / 100)
ret_tax = 1 - tax
take_home = (hours*pay)*ret_tax
print("$" + str(take_home) + " is your paycheck!" )