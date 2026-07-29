# Parking Fee Calculator

vehicle = input("Enter Vehicle Type (Bike/Car): ")
hours = int(input("Enter Parking Duration (Hours): "))

if vehicle.lower() == "bike":
    fee = hours * 20
elif vehicle.lower() == "car":
    fee = hours * 50
else:
    print("Invalid Vehicle Type")
    fee = 0

print("\n----- Parking Details -----")
print("Vehicle Type :", vehicle)
print("Parking Hours:", hours)
print("Parking Fee  : ₹", fee)