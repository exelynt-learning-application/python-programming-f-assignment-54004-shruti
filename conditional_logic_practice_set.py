# ----------------------------------------------------------
# Program: Conditional Logic Practice Set
# Module: Practice Programs
# Description:
# This file contains solutions to five conditional
# logic problems using Python.
# ----------------------------------------------------------

# ==========================================================
# Program 1: Check Whether a Number is Even or Odd
# ==========================================================

print("========== Program 1: Even or Odd ==========")

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is an Even number.")
else:
    print(f"{number} is an Odd number.")

print()


# ==========================================================
# Program 2: Check Whether a Year is a Leap Year
# ==========================================================

print("========== Program 2: Leap Year ==========")

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is Not a Leap Year.")

print()


# ==========================================================
# Program 3: Find the Largest of Three Numbers
# ==========================================================

print("========== Program 3: Largest of Three Numbers ==========")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print(f"The largest number is: {largest}")

print()


# ==========================================================
# Program 4: Check Whether a Number is Positive,
# Negative, or Zero
# ==========================================================

print("========== Program 4: Positive, Negative, or Zero ==========")

num = float(input("Enter a number: "))

if num > 0:
    print("The number is Positive.")
elif num < 0:
    print("The number is Negative.")
else:
    print("The number is Zero.")

print()


# ==========================================================
# Program 5: Determine Pass/Fail Based on Marks
# ==========================================================

print("========== Program 5: Pass or Fail ==========")

marks = float(input("Enter your marks: "))

if marks >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")

print("\nAll programs executed successfully!")
