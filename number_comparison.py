# ----------------------------------------------------------
# Program: Number Comparison Program
# Module: Comparison & Logical Operators
# Description:
# This program accepts two numbers from the user,
# compares them using comparison operators, and
# demonstrates logical operators (and, or, not).
# ----------------------------------------------------------

print("======================================")
print("      Number Comparison Program")
print("======================================\n")

# Take input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# ----------------------------------------------------------
# Comparison Operations
# ----------------------------------------------------------

print("\n========== Comparison Results ==========")

print(f"Is the first number greater than the second? : {num1 > num2}")
print(f"Is the second number greater than the first? : {num2 > num1}")
print(f"Are both numbers equal?                      : {num1 == num2}")

# ----------------------------------------------------------
# Logical Operations
# ----------------------------------------------------------

both_positive = (num1 > 0) and (num2 > 0)
at_least_one_positive = (num1 > 0) or (num2 > 0)
not_equal = not (num1 == num2)

print("\n========== Logical Results ==========")

print(f"Are both numbers positive?      : {both_positive}")
print(f"Is at least one number positive?: {at_least_one_positive}")
print(f"Are the numbers NOT equal?      : {not_equal}")

print("\nProgram executed successfully!")
