from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        while operation_symbol not in operations.keys():
            print("Please, pick a valid operation!")
            operation_symbol = input("Pick an operation: ")

        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        finish = input(f"Type '[Y]' to continue calculating with {answer}, type '[N]' to start a new calculation, or type '[F]' to stop the calculator: ")
        if finish.lower() == 'y':
            num1 = answer
        elif finish.lower() == 'f':
            print("Thanks for using PythonLator, seeya!")
            break
        else:
            should_continue = False
            calculator()
