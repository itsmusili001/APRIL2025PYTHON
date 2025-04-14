purchases=float(input("Enter value of purchases"))
if (purchases>=5000):
    discount =purchases*0.05
    print(f"Discount is kshs{discount}")
else:
    discount = purchases*0
    print(f"discount is kshs {discount}")

print("END of program")