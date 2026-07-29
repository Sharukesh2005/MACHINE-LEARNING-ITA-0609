# Accept marks of five subjects

m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))
m4 = float(input("Enter marks of Subject 4: "))
m5 = float(input("Enter marks of Subject 5: "))

# Calculate total and average
total = m1 + m2 + m3 + m4 + m5
average = total / 5

# Assign Grade
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
elif average >= 50:
    grade = "E"
else:
    grade = "F"

# Display Results
print("\n----- Result -----")
print("Total Marks =", total)
print("Average Marks =", average)
print("Grade =", grade)