# ---------------------------------------------------------
# Program: Student Profile Generator
# Description: Demonstrates variables, data types,
# dynamic typing, type checking, and simple operations.
# ---------------------------------------------------------

# Student details
student_name = "Rahul Sharma"      # String
age = 20                           # Integer
course_fee = 25000.50              # Float
is_enrolled = True                 # Boolean

# Display student details
print("========== Student Profile ==========")
print(f"Student Name      : {student_name}")
print(f"Age               : {age}")
print(f"Course Fee        : ₹{course_fee}")
print(f"Enrolled          : {is_enrolled}")

# Display data types
print("\n----- Data Types -----")
print("Student Name :", type(student_name))
print("Age          :", type(age))
print("Course Fee   :", type(course_fee))
print("Enrolled     :", type(is_enrolled))

# ----------------------------------------
# Dynamic Updates
# ----------------------------------------

# Increment student's age
age = age + 1

# Change enrollment status
is_enrolled = False

# Add 10% tax to the course fee
tax = course_fee * 0.10
course_fee = course_fee + tax

# Display updated details
print("\n========== Updated Student Profile ==========")
print(f"Student Name      : {student_name}")
print(f"Updated Age       : {age}")
print(f"Updated Course Fee: ₹{course_fee:.2f}")
print(f"Enrolled          : {is_enrolled}")

# Display updated data types
print("\n----- Updated Data Types -----")
print("Student Name :", type(student_name))
print("Age          :", type(age))
print("Course Fee   :", type(course_fee))
print("Enrolled     :", type(is_enrolled))

print("\nProgram executed successfully!")
