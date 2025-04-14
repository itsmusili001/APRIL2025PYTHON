age =int(input("Enter age "))

if age < 0:
    print("Error! age cannot be negative")
elif age <= 1:
    print("infant")
elif age <13:
    print("child")
elif age <20:
    print("teenager")
else:
    print("adult")