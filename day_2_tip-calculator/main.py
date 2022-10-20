total_bill = float(input("What was the total bill? $"))
percentage = input("What percentage tip would you like to give? 10, 12, 15?")
people = int(input("How many people to split the bill?"))

percent = (float(percentage) / 100) + 1


print(f"Each person should pay: ${round((total_bill / people) * percent, 2)}")