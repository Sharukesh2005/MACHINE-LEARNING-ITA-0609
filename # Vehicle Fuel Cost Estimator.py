# Vehicle Fuel Cost Estimator

distance = float(input("Enter Distance (km): "))
mileage = float(input("Enter Vehicle Mileage (km/litre): "))
fuel_price = float(input("Enter Fuel Price per litre: ₹"))

fuel_required = distance / mileage
fuel_cost = fuel_required * fuel_price

print("\n----- Fuel Cost Details -----")
print("Distance Travelled :", distance, "km")
print("Fuel Required      :", round(fuel_required, 2), "litres")
print("Fuel Cost          : ₹", round(fuel_cost, 2))