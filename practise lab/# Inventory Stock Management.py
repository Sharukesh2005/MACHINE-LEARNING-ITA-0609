# Inventory Stock Management

product = input("Enter Product Name: ")
stock = int(input("Enter Available Stock: "))
minimum = int(input("Enter Minimum Stock Level: "))

print("\nProduct :", product)
print("Available Stock :", stock)

if stock < minimum:
    print("Alert: Stock is below the minimum level.")
    print("Please Reorder the Product.")
else:
    print("Stock Level is Sufficient.")