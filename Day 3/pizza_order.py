print("Welcome to Python Pizza Deliveries!")

size = str
add_pepperoni = str
extra_cheese = str

while size not in ("S", "M", "L"):
    size = input("What size do you want (S, M or L)? ")

while add_pepperoni not in ("Y", "N"):
    add_pepperoni = input("Do you want pepperoni? (Y/N) ")

while extra_cheese not in ("Y", "N"):
    extra_cheese = input("Do you want some extra cheese? (Y/N) ")

if size == "S":
    price = 12.5
if size == "M":
    price = 18.30
if size == "L":
    price = 23.89

if add_pepperoni == "Y":
    price += 3.50

if extra_cheese == "Y":
    price += 4.50

print(f"The final price is US$ {round(price, 2)}.")
