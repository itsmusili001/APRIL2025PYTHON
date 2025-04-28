f=open("employees.txt","w")


for counter in range(5):
    name=input(f"enter the name for employee  {counter+1}:")
    age=input(f"enter the age for employee  {counter+1}:")
    department=input(f"enter the department for employee  {counter+1}:")
    f.write(f"Name: {name}, Age: {age}, Department: {department}\n")
f.close()
   