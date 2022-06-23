MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def ingredients_checker(coffee_type):
    for key in MENU[coffee_type]["ingredients"].keys():
        if MENU[coffee_type]["ingredients"][key] < resources[key]:
            print(f"Enough {key}")
        else:
            print(f"Sorry, there is not enough {key}.")


def cashier(coffee_type, given_money):
    price = MENU[coffee_type]["cost"]
    if price < given_money:
        change = given_money - price
        print(
            f"Here is your {change} change and your receipt. Thanks for visiting us!")
    elif price == given_money:
        print("Here is your receipt. Thanks for visiting us!")
    else:
        print(f"Sorry, you need to pay {round(price - given_money, 2)} more.")


coffee_type = input("​What would you like? espresso/latte/cappuccino?:")

ingredients_checker(coffee_type)
cashier(coffee_type, 2.10)
