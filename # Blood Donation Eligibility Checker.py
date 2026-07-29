# Blood Donation Eligibility Checker

age = int(input("Enter Age: "))
weight = float(input("Enter Weight (kg): "))
hemoglobin = float(input("Enter Hemoglobin Level (g/dL): "))

if age >= 18 and age <= 60 and weight >= 50 and hemoglobin >= 12.5:
    print("\nEligible for Blood Donation")
else:
    print("\nNot Eligible for Blood Donation")