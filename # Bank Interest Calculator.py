# Bank Interest Calculator

principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest (%): "))
time = float(input("Enter Time (Years): "))

simple_interest = (principal * rate * time) / 100

compound_amount = principal * ((1 + rate / 100) ** time)
compound_interest = compound_amount - principal

print("\n----- Interest Details -----")
print("Simple Interest      :", simple_interest)
print("Compound Interest    :", compound_interest)
print("Total Amount (CI)    :", compound_amount)