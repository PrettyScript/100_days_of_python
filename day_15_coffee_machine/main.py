from menu import resources, MENU

#TODO Print report
def report():
    money = 0
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")

# report()

#TODO Print coffee prices
def prices():
    print(f"Espresso:${MENU['espresso']['cost']}")
    print(f"Latte:${MENU['latte']['cost']}")
    print(f"Cappuccino:${MENU['cappuccino']['cost']}")

# prices()

#TODO Check resources sufficient 

#TODO Get Coffee Price
def get_coffee_price(coffee):
    price = MENU[coffee]['cost']
    return price

# get_coffee_price('espresso')

#TODO Process Coins
def process_coins():
    # call check resources then process 
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    quarter = .25
    dime = .10
    nickle = .05
    penny = .01
    coin_total = (quarter * quarters) + (dime * dimes) + (nickle * nickles) + (penny * pennies)
    print(coin_total)
    print(3.5 - coin_total)

# process_coins()

#TODO Check transaction successful?
# def check_transaction():

#TODO Make Coffee
coffee = '☕'

#TODO Turn off coffee machine
# def turn_off_machine(request):
#     '''Takes user input to end code execution'''



def coffee_machine_on():
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == 'report':
        report()
    elif order == 'espresso':
        process_coins()
    elif order == 'latte':
        process_coins()
    elif order == 'cappuccino':
        process_coins()
    elif order == 'off':
        turn_off_machine()
    