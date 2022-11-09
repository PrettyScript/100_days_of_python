from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True

# def report():



while is_on:
    menu = Menu()
    coffemaker = CoffeeMaker()
    moneymachine = MoneyMachine()
    moneymachine.profit = 0

    order = input(f"What would you like? ({menu.get_items()}): ")

    if order == 'off':
        is_on = False
    elif order == 'report':
        print(coffemaker.report())
        print(moneymachine.profit)
    else:
        drink = menu.find_drink(order)
        if coffemaker.is_resource_sufficient(drink):
            moneymachine.money_received = moneymachine.process_coins()
            if moneymachine.make_payment()
