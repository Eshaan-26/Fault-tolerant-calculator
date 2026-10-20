from num2words import num2words

def calculator(intake):
    while True:
        try:
            value = float(input(intake))
            return value
        except ValueError:
            print("Enter a valid number")


def addition():
    while True:
        try:
            total_additions = int(input("Enter the amount of numbers you want to add: "))
        except ValueError:
            print("Enter a valid number")
        else:
             total = 0
             for i in range(total_additions):
                num = calculator(f"Enter number {num2words(i+1)} : ")
                total += num
             return total
        

def multiplication():
    while True:
        try:
            total_multiplcations = int(input("Enter the amount of numbers you want to multiply: "))
        except ValueError:
            print("Enter an valid number")
        else:
            total = 1
            for i in range(total_multiplcations):
                num = calculator(f"Enter number {num2words(i+1)} :")
                total *= num
            return total


def division():
    num = calculator("Enter the number you want to divide: ")
    while True:
        try:
            num2 = calculator("Enter the number you want it to be divided with: ")
            if num2 == 0:
                raise ZeroDivisionError
        except ZeroDivisionError:
            print("Number cannot be divided by zero")
        else:
            total = num/num2
        return total

def subtraction():
    initial_num = float(input("Enter the number you want to subtract from: "))
    total_subtractions = int(input("Enter the amount of numbers you want to subtract: "))
    total = initial_num
    for i in range(total_subtractions):
        num = calculator(f"Enter number {num2words(i+1)} : ")
        total -= num 

    return total

while True:
    try:
        operations = input("Enter the operation you want to do +,-,*,/,end: ").strip()
        operation = operations.lower()
        if operation == "+":
            print(f'The total sum is {addition()}')
        elif operation == "-":
            print(f"The subtracted value is {subtraction()} ")
        elif operation == "*":
            print(f"The total value is {multiplication()}")
        elif operation == "/":
            print(f"The divided value is {division()}")
        elif operation == "end":
            print("Ending program")
            break
        else:
            raise ValueError

    except ValueError:
        print("Enter an correct operation")