# BMI Calculator

weight = float(input("Enter Weight (kg): "))
height = float(input("Enter Height (m): "))

bmi = weight / (height * height)

print("\nBMI =", round(bmi,2))

if bmi < 18.5:
    print("Health Status : Underweight")
elif bmi < 25:
    print("Health Status : Normal Weight")
elif bmi < 30:
    print("Health Status : Overweight")
else:
    print("Health Status : Obese")