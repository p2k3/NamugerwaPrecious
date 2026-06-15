#create a menu driven calculator(GUI) using function for addition,subtraction,multiplaction and division
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed"
    
while True: #user can do multiple calculation until they choose to exit
    print("Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '5':
        print("Exiting the calculator. Goodbye!")
        break
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    if choice == '1':
        result = add(num1, num2)
        print(f"The sum is: {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"The difference is: {result}")
    elif choice == '3':
        result = multiply(num1, num2)
        print(f"The product is: {result}")
    elif choice == '4':
     result = divide(num1, num2)
     if isinstance(result, str):  # Check if it's an error message (string)
        print(result)  # Just print the error message
     else:
        print(f"The quotient is: {result}")  # Print with label only if it's a number
    else:
        print("Invalid choice. Please try again.  ")


