# Employee Salary Calculation

# Input
basic_salary = float(input("Enter Basic Salary: "))
hra = float(input("Enter HRA: "))
da = float(input("Enter DA: "))

# Gross Salary
gross_salary = basic_salary + hra + da

# Deductions
pf = basic_salary * 0.12      # 12% of Basic Salary
tax = gross_salary * 0.10     # 10% of Gross Salary

# Net Salary
net_salary = gross_salary - (pf + tax)

# Output
print("\n----- Salary Details -----")
print("Basic Salary :", basic_salary)
print("HRA          :", hra)
print("DA           :", da)
print("Gross Salary :", gross_salary)
print("PF Deduction :", pf)
print("Tax          :", tax)
print("Net Salary   :", net_salary)