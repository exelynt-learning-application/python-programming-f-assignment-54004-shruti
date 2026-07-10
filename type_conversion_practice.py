# ---------------------------------------------------------
# Program: Type Conversion Practice Program
# Description:
# Demonstrates type casting, arithmetic operations,
# string conversion, and type checking in Python.
# ---------------------------------------------------------

print("====================================")
print("    Type Conversion Practice")
print("====================================")

# Accept user input
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Convert input to integer
int_num1 = int(num1)
int_num2 = int(num2)

# Convert input to float
float_num1 = float(num1)
float_num2 = float(num2)

# Display converted values and their data types
print("\n----- Converted Values -----")
print("Integer Value 1:", int_num1, "| Type:", type(int_num1))
print("Integer Value 2:", int_num2, "| Type:", type(int_num2))
print("Float Value 1  :", float_num1, "| Type:", type(float_num1))
print("Float Value 2  :", float_num2, "| Type:", type(float_num2))

# Perform arithmetic operations
print("\n----- Arithmetic Operations -----")
print("Addition       :", float_num1 + float_num2)
print("Subtraction    :", float_num1 - float_num2)
print("Multiplication :", float_num1 * float_num2)
print("Division       :", float_num1 / float_num2)

# Convert numeric value to string
string_value = str(int_num1)

print("\n----- String Conversion -----")
print("The first number as a string is:", string_value)
print("Data Type:", type(string_value))

print("\nProgram executed successfully!")
