from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
coffee_maker = CoffeeMaker()
cash_machine = MoneyMachine()

items = coffee_menu.get_items() # get menu items


is_on = True
while is_on:
    choice = input(f"What would you like? ({items}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        cash_machine.report()
    else:
        drink = coffee_menu.find_drink(choice)
        if drink != None:
            if coffee_maker.is_resource_sufficient(drink) and cash_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


