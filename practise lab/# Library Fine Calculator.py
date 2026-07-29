# Library Fine Calculator

days = int(input("Enter Number of Overdue Days: "))

if days <= 5:
    fine = days * 2
elif days <= 10:
    fine = days * 5
else:
    fine = days * 10

print("\nLibrary Fine = ₹", fine)