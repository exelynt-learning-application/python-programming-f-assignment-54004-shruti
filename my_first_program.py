# ----------------------------------------------------------
# Program: My First Python Program
# Description:
# This program demonstrates variables, input/output,
# type casting, arithmetic operations, and type checking.
# ----------------------------------------------------------

# Display program title
print("=======================================")
print("        My First Python Program")
print("=======================================\n")

# ----------------------------------------------------------
# Step 1: Get user input
# ----------------------------------------------------------

# Read user's name (string)
name = input("Enter your name: ")

# Read user's age and convert it to integer
age = int(input("Enter your age: "))

# Read user's height and convert it to float
height = float(input("Enter your height (in meters): "))

# Read user's favorite number and convert it to float
favorite_number = float(input("Enter your favorite number: "))

# ----------------------------------------------------------
# Step 2: Perform arithmetic operation
# ----------------------------------------------------------

# Add age and favorite number
total = age + favorite_number

# ----------------------------------------------------------
# Step 3: Display user information
# ----------------------------------------------------------

print("\n=======================================")
print("            USER DETAILS")
print("=======================================")

print(f"Name             : {name}")
print(f"Age              : {age} years")
print(f"Height           : {height} meters")
print(f"Favorite Number  : {favorite_number}")

# ----------------------------------------------------------
# Step 4: Display data types
# ----------------------------------------------------------

print("\n--------- Data Types ---------")
print("Name             :", type(name))
print("Age              :", type(age))
print("Height           :", type(height))
print("Favorite Number  :", type(favorite_number))

# ----------------------------------------------------------
# Step 5: Display arithmetic result
# ----------------------------------------------------------

print("\n--------- Arithmetic Operation ---------")
print(f"Age + Favorite Number = {total}")

# ----------------------------------------------------------
# End of program
# ----------------------------------------------------------

print("\nThank you for using My First Python Program!")
print("Program executed successfully.")
