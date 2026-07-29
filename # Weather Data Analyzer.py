# Weather Data Analyzer

temperature = []

print("Enter Temperature for 7 Days")

for i in range(7):
    temp = float(input(f"Day {i+1}: "))
    temperature.append(temp)

maximum = max(temperature)
minimum = min(temperature)
average = sum(temperature) / len(temperature)

print("\n----- Weather Report -----")
print("Temperatures :", temperature)
print("Maximum Temperature :", maximum)
print("Minimum Temperature :", minimum)
print("Average Temperature :", round(average, 2))