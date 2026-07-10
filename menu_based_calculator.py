# ----------------------------------------------------------
# Program: Menu-Based Calculator Using match-case
# Module: match-case Statement
# Description:
# This program performs basic arithmetic operations
# based on the user's menu choice using the
# match-case statement.
# ----------------------------------------------------------

print("======================================")
print("      Menu-Based Calculator")
print("======================================")

# Display menu
print("\nSelect an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Get user choice
choice = int(input("\nEnter your choice (1-4): "))

# Get two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("\n========== Result ==========")

# Perform operation using match-case
match choice:
    case 1:
        result = num1 + num2
        print(f"Addition = {result}")

    case 2:
        result = num1 - num2
        print(f"Subtraction = {result}")

    case 3:
        result = num1 * num2
        print(f"Multiplication = {result}")

    case 4:
        if num2 != 0:
            result = num1 / num2
            print(f"Division = {result}")
        else:
            print("Error: Division by zero is not allowed.")

    case _:
        print("Invalid choice! Please select a number between 1 and 4.")

print("\nProgram executed successfully!")
