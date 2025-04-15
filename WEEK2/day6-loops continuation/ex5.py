#using a while loop for input validation
total=0
for counter in range(1,11):
    price = float(input("enter price of item\n"))
    while price<0:
        print("Enter a valid price >=0")
        price = float(input("enter price of item\n"))
    total = total+price
print(f"The total price for 10 items is {total:.2f} ")