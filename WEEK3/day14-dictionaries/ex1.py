#a dictionary is a collection of key-value pairs
students = {"name": "Anne",
"age": 21, 
"course": ["python", "java", "web design", "Discrete math"],
"nationality": "Kenyan",
"idNo": 123456,
"tel": 1234567890,}



#declaring a dictionary using a method constructor
driver=dict(name="Anne",dlClass="BCE",LicenseNo="111111")
print(type(students)) 
print(type(driver)) 
print(students)
print(driver)

#accessing values in a dictionary using keys
print(students["name"])
print(driver["LicenseNo"])

students["name"] = "Anita"
print(students["name"])

#deleting a key-value pair from a dictionary
del students["nationality"]
print(students)

#getting the length of a dictionary
print(len(students))

