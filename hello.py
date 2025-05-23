print("Hello, world!")
# create a basic calculator
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y    
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
# take input from the user
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if choice == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif choice == '3':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif choice == '4':
    if num2 != 0:
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid input")

    

# This is a simple calculator program that performs addition, subtraction, multiplication, and division.
# It takes two numbers and an operation as input from the user and prints the result.
# The program also handles division by zero error.
# The calculator supports four operations: addition, subtraction, multiplication, and division.
# The program uses functions to perform each operation and takes user input for the numbers and the operation.
# The program is written in Python and can be run in any Python environment.
# The calculator can be extended to include more operations such as exponentiation, modulus, etc.
# The calculator can also be improved by adding error handling for invalid inputs and edge cases.
# The calculator can be used for basic arithmetic calculations and can be a useful tool for students and professionals.
# The calculator can be further enhanced by adding a graphical user interface (GUI) using libraries like Tkinter or PyQt.
# The calculator can also be made more user-friendly by adding features like history, memory, and scientific functions.
# The calculator can be used in various fields such as engineering, finance, and education.
# The calculator can be a great learning tool for beginners to understand the basics of programming and arithmetic operations.




