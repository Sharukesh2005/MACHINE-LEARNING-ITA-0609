# Mobile Recharge Billing

amount = float(input("Enter Recharge Amount: ₹"))

if amount >= 500:
    discount = amount * 0.10
elif amount >= 300:
    discount = amount * 0.05
else:
    discount = 0

final_amount = amount - discount

print("\n----- Recharge Bill -----")
print("Recharge Amount : ₹", amount)
print("Discount        : ₹", discount)
print("Final Amount    : ₹", final_amount)