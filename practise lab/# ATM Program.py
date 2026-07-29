# ATM Program

# Initial Details
correct_pin = 1234
balance = 10000

# Input PIN
pin = int(input("Enter your PIN: "))

# Verify PIN
if pin == correct_pin:
    print("\nPIN Verified Successfully")
    print("Available Balance: ₹", balance)

    # Enter withdrawal amount
    amount = float(input("Enter amount to withdraw: ₹"))

    if amount <= balance:
        balance = balance - amount
        print("\nWithdrawal Successful!")
        print("Amount Withdrawn: ₹", amount)
        print("Remaining Balance: ₹", balance)
    else:
        print("\nInsufficient Balance!")

else:
    print("\nInvalid PIN!")