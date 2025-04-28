f=open("numbers.txt","w")
for counter in range(7):
    number =input(f"enter the number {counter+1}:")
    f.write(f"{number}\n")
f.close()  
total = 0
f=open("numbers.txt","r")

for line in f:
    total += int(line.strip())
print(f"The total is {total}")