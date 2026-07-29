# Movie Ticket Booking System

seats = int(input("Enter Number of Seats: "))
category = input("Enter Seat Category (Silver/Gold): ")

if category.lower() == "silver":
    price = 150
elif category.lower() == "gold":
    price = 250
else:
    print("Invalid Category")
    exit()

total = seats * price

# Discount
if total >= 1000:
    discount = total * 0.10
else:
    discount = 0

final_amount = total - discount

print("\n----- Movie Ticket Bill -----")
print("Seat Category :", category)
print("Number of Seats :", seats)
print("Ticket Cost : ₹", total)
print("Discount : ₹", discount)
print("Final Amount : ₹", final_amount)