#a program that uses loop to display number of calories burned after 10,15,20,25,30 minute


for minutes in range (10,31,5):
    calories_burned=minutes*4.2
    
print(input("enter calries burned"))
print(f"calories burned per minute{calories_burned:.4f}")


