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
            "water": 200,
            "milk": 100,
            "coffee": 24,

        },
        "cost": 3.0,
    }

}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_sufficient (choice):
    """Returns False if there is not enough resources tho make a drink."""
    for key in MENU[choice]["ingredients"]:
        if MENU[choice]["ingredients"][key] >= resources[key]:
            print(f"Sorry there is not enough {key}")
            return False
    return True

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins. ")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01

    return round(total, 2)

def make_drink(choice, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Enjoy your {choice}")

def is_enough_money(choice, total):
    """Returns False if there is not enough money"""
    cost = int(MENU[choice]["cost"])
    if total < cost:
        print("Sorry you did not inserted enough money.")
        return False
    global profit
    profit += cost
    change = round(total - cost, 2)
    print(f"Your change is {change}")
    return True

coffee_machine_on = True

while coffee_machine_on:
    choice = input("What would you like coffee, latte or cappuccino?  ")
    if choice.lower() == "off":
        coffee_machine_on = False
    elif choice.lower() == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${profit}")
    else:
        if check_sufficient(choice):
            total = process_coins()
            print(f"You have inserted ${total}")
            if is_enough_money(choice, total):
                make_drink(choice, MENU[choice]["ingredients"])

