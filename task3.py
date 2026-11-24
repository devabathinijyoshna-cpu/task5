consultation = float(input("Enter consultation charges: "))
diagnostic = float(input("Enter diagnostic charges: "))
treatment = float(input("Enter treatment charges: "))

total = consultation + diagnostic + treatment

if total >= 10000:
    discount = total * 0.10
elif total >= 5000:
    discount = total * 0.05
else:
    discount = 0

final_bill = total - discount

print("Total Bill:", total)
print("Discount:", discount)
print("Final Bill:", final_bill)