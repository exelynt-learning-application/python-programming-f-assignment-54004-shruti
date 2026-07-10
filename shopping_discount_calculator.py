# ----------------------------------------------------------
# Program: Shopping Discount Calculator
# Module: Real-Life Decision Examples
# Description:
# This program calculates the discount and final payable
# amount based on the total purchase amount entered by the user.
# ----------------------------------------------------------

print("======================================")
print("     Shopping Discount Calculator")
print("======================================\n")

# Take total purchase amount as input
purchase_amount = float(input("Enter the total purchase amount (₹): "))

# Initialize variables
discount_percentage = 0
discount_amount = 0

# ----------------------------------------------------------
# Apply discount rules
# ----------------------------------------------------------

if purchase_amount >= 5000:
    discount_percentage = 20
elif purchase_amount >= 3000:
    discount_percentage = 10
else:
    discount_percentage = 0

# Calculate discount and final payable amount
discount_amount = (purchase_amount * discount_percentage) / 100
final_amount = purchase_amount - discount_amount

# ----------------------------------------------------------
# Display bill details
# ----------------------------------------------------------

print("\n======================================")
print("         SHOPPING BILL")
print("======================================")
print(f"Purchase Amount   : ₹{purchase_amount:.2f}")
print(f"Discount          : {discount_percentage}%")
print(f"Discount Amount   : ₹{discount_amount:.2f}")
print(f"Final Amount      : ₹{final_amount:.2f}")
print("======================================")

print("\nThank you for shopping with us!")
print("Program executed successfully.")
