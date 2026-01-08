# ================================
# Advanced Calculator Program
# ================================

history = []

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def modulus(a, b):
    if b == 0:
        return "Error: Modulus by zero"
    return a % b

def power(a, b):
    return a ** b

def show_menu():
    print("\n------ CALCULATOR MENU ------")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (**)")
    print("7. View History")
    print("8. Exit")
    print("-----------------------------")

while True:
    show_menu()
    choice = input("Enter your choice (1-8): ")

    if choice == '8':
        print("Calculator Closed. Thank you!")
        break

    if choice == '7':
        print("\n--- Calculation History ---")
        if not history:
            print("No calculations yet.")
        else:
            for item in history:
                print(item)
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        continue

    if choice == '1':
        result = add(num1, num2)
        operation = f"{num1} + {num2} = {result}"

    elif choice == '2':
        result = subtract(num1, num2)
        operation = f"{num1} - {num2} = {result}"

    elif choice == '3':
        result = multiply(num1, num2)
        operation = f"{num1} * {num2} = {result}"

    elif choice == '4':
        result = divide(num1, num2)
        operation = f"{num1} / {num2} = {result}"

    elif choice == '5':
        result = modulus(num1, num2)
        operation = f"{num1} % {num2} = {result}"

    elif choice == '6':
        result = power(num1, num2)
        operation = f"{num1} ** {num2} = {result}"

    else:
        print("Invalid choice! Try again.")
        continue

    print("Result:", result)
    history.append(operation)
