# ---------------------------------------------------------
# Program: Basic Python Structure Demonstration
# Description: Demonstrates Python syntax and indentation.
# ---------------------------------------------------------

# Program title
print("===================================")
print(" Basic Python Structure Demonstration")
print("===================================")

# Top-level print statements
print("Welcome to the Python syntax example.")
print("This program demonstrates indentation.")
print("Python uses indentation to define code blocks.")

number = 10

# Start of the if block
# Indentation is required because Python uses spaces
# to identify which statements belong to the if block.
if number > 5:
    print("\nThe number is greater than 5.")

    # Start of the nested block
    # This nested if statement is indented further because
    # it belongs inside the first if block.
    if number == 10:
        print("The number is exactly 10.")
        print("This is a nested block example.")
    # End of nested if block

    print("Execution continues inside the outer if block.")
# End of outer if block

print("\nProgram executed successfully.")
print("Thank you for using this demonstration.")
