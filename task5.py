usage = int(input("Enter data usage in GB: "))
budget = float(input("Enter your budget: "))

plans = [199, 299, 399, 499]
data = [10, 20, 30, 50]

best = -1

for i in range(len(plans)):
    if data[i] >= usage and plans[i] <= budget:
        if best == -1 or plans[i] < plans[best]:
            best = i

if best != -1:
    print("Best Plan Price:", plans[best])
    print("Data Limit:", data[best], "GB")
else:
    print("No suitable plan available")