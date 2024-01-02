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

money = 0

# FUNCTIONS

# Display Report
def show_report(resources, cash):
    for ingredient in resources:
        if (ingredient != "coffee"):
            print(f"{ingredient.title()}: {resources[ingredient]}ml")
        else:
            print(f"{ingredient.title()}: {resources[ingredient]}g")
    print(f"Money: ${round(cash, 2)}")

# Make coffee, deplete resources
def make_coffee(obj, resources):
    ingredients = obj["ingredients"]
    for ingredient in ingredients:
        resources[ingredient] = resources[ingredient] - ingredients[ingredient]
    return resources

# Check resources in machine
def check_resources(obj, resources):
    ingredients = obj["ingredients"]
    for key in ingredients:
        if ingredients[key] > resources[key]:
            return f"Sorry, there is not enough {key}"
    return

# Calculate amount paid in coins
def calculate_coins(quarters, dimes, nickles, pennies):
    total = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    return total

# Check if resources sufficient
def check_sufficient(obj, amount_paid):
    total = amount_paid
    cost = obj["cost"]
    if (total > cost):
        return True
    else:
        return False
    


drink = input("What would you like? (espresso/latte/cappuccino): ")
while drink != 'off':

    if (drink == 'report'):
        show_report(resources, money)
        drink = input("What would you like? (espresso/latte/cappuccino): ")

    else:

        if check_resources(MENU[drink], resources) == None:
            print("Please insert coins")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))

            amount_paid = calculate_coins(quarters, dimes, nickles, pennies)
            if check_sufficient(MENU[drink], amount_paid):
                money += MENU[drink]["cost"]
                change = amount_paid - MENU[drink]["cost"]

                resources = make_coffee(MENU[drink], resources)

                print(f"Here is ${round(change, 2)} in change.")
                print(f"Here is your {drink} ☕️ Enjoy!")

                drink = input("What would you like? (espresso/latte/cappuccino): ")
            else:
                print(f"Sorry that's not enough money, money refunded.")
                drink = input("What would you like? (espresso/latte/cappuccino): ")
        else:
            print(check_resources(MENU[drink], resources))
            drink = input("What would you like? (espresso/latte/cappuccino): ")
    

        
        



