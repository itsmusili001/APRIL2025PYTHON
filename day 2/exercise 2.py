amount_of_purchase =float(input("Enter the amount of purchase"))
state_sales = 0.05
county_sales = 0.025

state_sales = amount_of_purchase*state_sales
county_sales = amount_of_purchase*county_sales
total_sales = state_sales + county_sales
total_amount = amount_of_purchase + total_sales

print(f"Amount of purchase: ${amount_of_purchase:.2f}")
print(f"State sales tax: ${state_sales:.2f}")
print(f"county sales tax: ${county_sales:.2f}")
print(f"total amount: ${total_amount:.2f}")
