# ----------------------------------------------------------
# Program: Loan Eligibility Checker
# Module: Nested Conditions
# Description:
# This program checks whether a user is eligible
# for a loan using nested if statements.
# Eligibility Criteria:
# 1. Age must be 21 years or above.
# 2. Salary must be ₹25,000 or above.
# ----------------------------------------------------------

print("======================================")
print("      Loan Eligibility Checker")
print("======================================\n")

# Take user input
age = int(input("Enter your age: "))
salary = float(input("Enter your monthly salary (₹): "))

# ----------------------------------------------------------
# Check eligibility using nested if statements
# ----------------------------------------------------------

# First, check the age requirement
if age >= 21:

    # If age is valid, check the salary requirement
    if salary >= 25000:
        print("\nCongratulations!")
        print("You are eligible to apply for the loan.")
    else:
        print("\nSorry!")
        print("You are not eligible because your monthly salary is less than ₹25,000.")

else:
    print("\nSorry!")
    print("You are not eligible because your age is below 21 years.")

print("\nThank you for using the Loan Eligibility Checker!")
print("Program executed successfully.")
