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
def check_resources(coffee):
    water_ingredient = MENU[coffee]['ingredients']['water']
    milk_ingredient = MENU[coffee]['ingredients']['milk']
    coffee_ingredient = MENU[coffee]['ingredients']['coffee']

    water_resource = resources['water']
    milk_resource = resources['milk']
    coffee_resource = resources['coffee']

    if coffee == 'espresso':
        return water_resource > water_ingredient and coffee_resource > coffee_ingredient
    elif coffee == 'latte' or coffee == 'cappuccino':
        return water_resource > water_ingredient and milk_resource > milk_ingredient and coffee_resource > coffee_ingredient

# check_resources('latte')

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
    return coin_total

# process_coins()

#TODO Check transaction successful?
def check_transaction(coffee):
    coins = process_coins()
    if coins >= get_coffee_price(coffee):
        # make_coffee()
        if coins > get_coffee_price(coffee):
           refund = get_coffee_price(coffee) - coins
           refund = round(abs(refund), 2)
           print(f"Here is ${refund} dollars in change.")
        print("Make coffee")
    else:
        print("Sorry that's not enough money. Money refunded.")

# check_transaction('espresso')

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
    # elif order == 'off':
    #     turn_off_machine()
    