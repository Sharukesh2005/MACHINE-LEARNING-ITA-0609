# Railway Ticket Fare Calculator

base_fare = 500

age = int(input("Enter Passenger Age: "))
travel_class = input("Enter Class (First/Second): ")

fare = base_fare

if travel_class.lower() == "first":
    fare += 300

if age < 12:
    fare *= 0.50
elif age >= 60:
    fare *= 0.70

print("\n----- Ticket Details -----")
print("Ticket Fare = ₹", fare)