# ----------------------------------------------------------
# Program: Hello World Python Program
# Module: Week 1 Final Test
# Description:
# This program demonstrates a simple Hello World program,
# user input, variables, formatted output, and comments.
# ----------------------------------------------------------

# Display a welcome message
print("=====================================")
print("      Hello World Python Program")
print("=====================================\n")

# Print Hello World
print("Hello, World!")
print("Welcome to Python Programming!\n")

# ----------------------------------------------------------
# Take user input
# ----------------------------------------------------------

# Get the user's name
name = input("Enter your name: ")

# Get the user's age and convert it to an integer
age = int(input("Enter your age: "))

# Get the user's city
city = input("Enter your city: ")

# ----------------------------------------------------------
# Display user information
# ----------------------------------------------------------

print("\n=====================================")
print("         USER INFORMATION")
print("=====================================")

print(f"Name : {name}")
print(f"Age  : {age}")
print(f"City : {city}")

# ----------------------------------------------------------
# Display data types of variables
# ----------------------------------------------------------

print("\nData Types:")
print("Name :", type(name))
print("Age  :", type(age))
print("City :", type(city))

# ----------------------------------------------------------
# End of program
# ----------------------------------------------------------

print("\nThank you for using this program!")
print("Program executed successfully.")
