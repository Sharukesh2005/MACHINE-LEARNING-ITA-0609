# Online Voting Eligibility Checker

age = int(input("Enter Age: "))
nationality = input("Enter Nationality: ")

if age >= 18 and nationality.lower() == "indian":
    print("\nEligible to Vote")
else:
    print("\nNot Eligible to Vote")