# Assignment 1
# Tasks 1, 2, & 3

#created functions for each arithmetic operation
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

#input from user using try statement to catch errors
try:
    x = float(input("Enter first number: "))
    arithmetic_op = input("Which operation would you like to use? Type add, subtract, multiply, or divide: ").lower()
    y = float(input("Enter second number: "))

    if arithmetic_op == 'add':
        result = add(x, y)
    elif arithmetic_op == 'subtract':
        result = subtract(x, y)
    elif arithmetic_op == 'multiply':
        result = multiply(x, y)
    elif arithmetic_op == 'divide':
        result = divide(x, y)
    else:
        raise ValueError("Invalid operation selected.")
    
    print(f"The result is: {result}")

#catching errors
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")