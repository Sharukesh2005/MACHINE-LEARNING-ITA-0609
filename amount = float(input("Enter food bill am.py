amount = float(input("Enter food bill amount: ₹"))

gst = amount * 0.05
service_charge = amount * 0.10

total = amount + gst + service_charge

print("\nFood Bill")
print("GST (5%) = ₹", gst)
print("Service Charge (10%) = ₹", service_charge)
print("Total Bill = ₹", total)