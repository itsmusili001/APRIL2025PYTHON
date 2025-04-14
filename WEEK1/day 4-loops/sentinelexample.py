proceed=True
total_expenses=0

budgetAmount=float(input("Enter the amount you have budgeted for this month"))
while proceed:
    expenses=float(input("Enter the current expense"))
    total_expenses=total_expenses +expenses
    print("do you wish to continue Enter y(yes) or any other key(No)")
    response=input()
    if response.lower() !='y':
        proceed=False
print(f"monthly budget minus Totalexpenses  is kshs{budgetAmount - total_expenses:.2f}")

