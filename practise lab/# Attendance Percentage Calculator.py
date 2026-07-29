# Attendance Percentage Calculator

total_classes = int(input("Enter Total Classes Conducted: "))
attended = int(input("Enter Classes Attended: "))

attendance = (attended / total_classes) * 100

print("\nAttendance Percentage =", round(attendance, 2), "%")

if attendance >= 75:
    print("Status : Eligible for Examination")
else:
    print("Status : Not Eligible for Examination")