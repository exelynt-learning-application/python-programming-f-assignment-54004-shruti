# ----------------------------------------------------------
# Program: Student Grade Calculator
# Module: if, elif, else Statements
# Description:
# This program accepts a student's marks,
# assigns a grade, handles invalid input,
# and displays the result.
# ----------------------------------------------------------

print("======================================")
print("      Student Grade Calculator")
print("======================================\n")

# Take marks as input
marks = float(input("Enter the student's marks (0 - 100): "))

# Check for valid marks
if marks < 0 or marks > 100:
    print("\nInvalid marks! Please enter marks between 0 and 100.")

# Assign grades
elif marks >= 90:
    print("\nGrade : A")
    print("Result: Excellent!")

elif marks >= 75:
    print("\nGrade : B")
    print("Result: Very Good!")

elif marks >= 60:
    print("\nGrade : C")
    print("Result: Good!")

else:
    print("\nGrade : Fail")
    print("Result: Better luck next time.")

print("\nProgram executed successfully!")
