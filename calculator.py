# Simple Calculator Program
# Author: Dual Ador Arok

def display_intro():
    print("Welcome to Dual's Mini Calculator!")
    print("You can perform basic math operations: +, -, *, /")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operation():
    operations = ['+', '-', '*', '/']
    while True:
        op = input("Choose an operation (+, -, *, /): ").strip()
        if op in operations:
            return op
        else:
            print("Operation not recognized. Try again.")

def calculate(x, y, op):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        if y == 0:
            return "Error: Division by zero is undefined."
        return x / y

def main():
    display_intro()
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    operation = get_operation()
    result = calculate(num1, num2, operation)

    print(f"\nResult: {num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    main()
