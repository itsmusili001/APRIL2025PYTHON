year=int(input("Enter year"))
if year%100==0 and year%400==0:
    print("29 days")
    print("leap year")
elif year%100!=0 and year%4==0:
     print("29 days")
     print("leap year")
else:
     print(" 28 days")
     print("not a leap year")
