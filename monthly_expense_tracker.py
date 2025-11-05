# Monthly Expense Tracker - Level 2
# A program to track monthly income and expenses

Monthly_income=int(input("enter the monthly salary "))
rent=int (input("enter the monthly rent "))
food=int (input("enter the monthly food expens "))
transportation=int(input("enter the transporation "))
entertainment=int(input("enter the  monthly expenses of  enterainment"))
#Different_categories=(rent, food, transportation, entertainment)
total_expenses= rent+food+transportation+entertainment
print(total_expenses)
remain= Monthly_income - total_expenses
print(f"monthly income {Monthly_income}")
print(f"expenses ,rent {rent},entertainment {entertainment},food {food}, transporation {transportation}")
print(f"remaining {remain}")
#IF total expenses are MORE than income → warn the user "You're overspending!"
#ELSE → say "Good job, you're within budget!"
if total_expenses>Monthly_income:
    print("You're overspending!")
else:
    print("Good job, you're within budget")
 
percentage=Monthly_income*0.2
if remain<percentage:
    print("Try to save more!")
else:
    print(" Great savings")
#Calculate 30% of income
thirtypercentage=Monthly_income*0.3
if rent>thirtypercentage:
    print("Rent is too high")
else:
    print("Rent is reasonable")
if food>thirtypercentage:
    print("food is too high")
else:
    print("food  is reasonable")
if transportation> thirtypercentage:
    print("transport is too high")
else:print("transport is reasonable")
if entertainment>thirtypercentage:
    print("entertainment is too high")
else:
    print("entertainment is reasonable")