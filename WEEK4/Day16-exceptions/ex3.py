
from random import randint
random_number = int(input("Enter the number of random numbers: "))

try:
    f=open("random_numbers.txt", "w")
except:
    print("an error occurred while opening the file")
for count in range(1,random_number+1):
    num=randint(1,500)
    f.write(str(num)+"\n")
    print(f"Random number {count} is {num}")
