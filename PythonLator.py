print("Welcome to the PythonLator!")

while True:
    operation = int(input("What operation do you want to do?\n1 - sum\n2 - subtraction\n3 - multiplication\n4 - division\n5 - exit\n"))
    if operation == 5:
        print("Thanks for using PythonLator, have a nice day!")
        break
    n1 = float(input("Type the first number: "))
    n2 = float(input("Now, the second one: "))
    if operation == 1:
        print(f"The result of the sum was: {n1 + n2 :.0f}")
    elif operation == 2:
        print(f"The result of the subtraction was: {n1 - n2 :.0f}")
    elif operation == 3:
        print(f"The result of the multiplication was: {n1 * n2 :.0f}")
    elif operation == 4:
        print(f"The result of the division was: {n1 // n2 :.0f}")
    else:
        print("Type a valid number!")
    repeat = input("Do you want to perform another operation?\n[Y]es [N]o\n")
    if repeat.upper() == "N":
        print("Thanks for using PythonLator, have a nice day!")
        break