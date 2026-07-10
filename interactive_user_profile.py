# ---------------------------------------------------------
# Program: Interactive User Profile Program
# Module : Input & Output Operations
# Description: Collects user details and displays them
#              in a formatted profile.
# ---------------------------------------------------------

# Display program title
print("===================================")
print("     INTERACTIVE USER PROFILE")
print("===================================\n")

# Accept user input
name = input("Enter your full name: ")
age = input("Enter your age: ")
gender = input("Enter your gender: ")
city = input("Enter your city: ")
occupation = input("Enter your occupation: ")

# Display user profile
print("\n===================================")
print("          USER PROFILE")
print("===================================")
print("Name       :", name)
print("Age        :", age)
print("Gender     :", gender)
print("City       :", city)
print("Occupation :", occupation)
print("===================================")

# Closing message
print("\nThank you for providing your details!")
print("Your profile has been created successfully.")
