print("Welcome to the tip calculator! \n")
total_bill = float(input("What was the total bill? \n"))
people_split = int(input("How many people to split the bill? \n"))
tip_percentage = float(input("What percentage tip would you like to give? \n"))

value_per_person = round((total_bill * (1 + tip_percentage / 100)) / people_split, 2)

print("Each person should pay US$ " + str(value_per_person))
