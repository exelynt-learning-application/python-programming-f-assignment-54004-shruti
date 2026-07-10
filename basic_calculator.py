# ----------------------------------------------------------
# Program: Basic Calculator Program
# Module: Arithmetic & Assignment Operators
# Description:
# This program accepts two numbers from the user,
# performs arithmetic operations, demonstrates
# assignment operators, and displays the results.
# ----------------------------------------------------------

print("======================================")
print("       Basic Calculator Program")
print("======================================\n")

# Take input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# ----------------------------------------------------------
# Arithmetic Operations
# ----------------------------------------------------------

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
modulus = num1 % num2

# Display arithmetic results
print("\n========== Arithmetic Operations ==========")
print(f"Addition       : {addition}")
print(f"Subtraction    : {subtraction}")
print(f"Multiplication : {multiplication}")
print(f"Division       : {division}")
print(f"Modulus        : {modulus}")

# ----------------------------------------------------------
# Assignment Operators
# ----------------------------------------------------------

assignment_value = num1

print("\n========== Assignment Operators ==========")
print(f"Initial Value : {assignment_value}")

assignment_value += num2
print(f"After +=      : {assignment_value}")

assignment_value -= num2
print(f"After -=      : {assignment_value}")

assignment_value *= num2
print(f"After *=      : {assignment_value}")

print("\nProgram executed successfully!")
