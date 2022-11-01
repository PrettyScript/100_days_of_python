# Calculator

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = int(input("What's the first number? "))
    for symbol in operations:
        print(symbol)
    calculator_on = True

    while calculator_on:
        operation_symbol = input("Pick an operation: ")
        num2 = int(input("What's the next number? "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        continue_operation = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit. ")

        if continue_operation == "y":
            # operation_symbol = input("Pick an operation: ")
            # num3 = int(input("What's the next number? "))
            # print(f"{answer} {operation_symbol} {num3} = {first_answer}")
            num1 = answer
        else:
            calculator_on = False
calculator()
