# Bill Calculation with Discount and GST

# Input Purchase Amount
amount = float(input("Enter Purchase Amount: ₹"))

# Calculate Discount
if amount < 1000:
    discount = 0
elif amount < 5000:
    discount = amount * 0.10
else:
    discount = amount * 0.20

# Amount after Discount
discounted_amount = amount - discount

# Calculate GST (18%)
gst = discounted_amount * 0.18

# Final Bill
total_bill = discounted_amount + gst

# Display Result
print("\n----- Bill Details -----")
print("Purchase Amount : ₹", amount)
print("Discount        : ₹", discount)
print("Amount After Discount : ₹", discounted_amount)
print("GST (18%)       : ₹", gst)
print("Total Bill      : ₹", total_bill)