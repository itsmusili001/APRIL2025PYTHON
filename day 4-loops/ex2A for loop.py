#program to calculate totals sales of the week
total_sales=0
max_sale=0
best_day=1
for counter in range(1,8,1):
    day_sales=float(input(f"Enter sales for day-{counter}-"))
    total_sales= total_sales + day_sales
    if day_sales > max_sale:
        max_sale=day_sales
        best_day=counter
print(f"Total sales of the week kshs:{total_sales:.2f}")
print(f"best day was -:day{best_day} with sales of {max_sale}")
