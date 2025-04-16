sales=[]
days=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
print("enter the sales for each day of the week")
for day in days:
    sale=float(input(f"enter the sales for the {day}:"))
    sales.append(sale)
total_sales=sum(sales)
print(f"the total sales for the week are: kshs{total_sales:.2f}")
