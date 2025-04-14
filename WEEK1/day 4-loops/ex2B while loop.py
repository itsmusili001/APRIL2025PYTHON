total_sales=0
max_sale=0
best_day=1

counter=1
while(counter<8): 
    day_sales=float(input(f"Enter sales for day-{counter}-"))
    total_sales= total_sales + day_sales
    if day_sales > max_sale:
        max_sale=day_sales
        best_day=counter
    counter=counter+1 #alternatively you can use counter +=1
print(f"Total sales of the week kshs:{total_sales:.2f}")
print(f"best day was -:day{best_day} with sales of {max_sale}")
