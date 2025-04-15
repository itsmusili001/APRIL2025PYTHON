loan_payment=float(input("Enter the monthly loan payment:-"))
insurance=float(input("Enter the monthly insuarance cost:-"))
gas=float(input("Enter the monthly gas cost:-"))
oil=float(input("Enter the monthly  oil cost:-"))
tires=float(input("Enter the monthly tires cost:-"))
maintenance=float(input("Enter the monthly maintenance cost:-"))

total_monthly_cost=loan_payment+insurance+gas+oil+tires+maintenance
total_anual_cost=total_monthly_cost*12

print("\n total monthly cost:kshs{:.2f}".format(total_monthly_cost))
print("\n total annual cost:kshs{:.2f}".format(total_anual_cost))

