zeros=[0]*10
print(zeros)

rangelist=list(range(1,11))
print(rangelist)
 

rangelist2=list(range(100,95, -1))
print(rangelist2)
x=len(rangelist)  #length of the list or number items in the list
print(x)

eaCountries=["Kenya","Uganda","Tanzania","Rwanda","Burundi"]

countries2=eaCountries #does not create a copy of the list but,points to the same list  

print(countries2) 

copyCountries=eaCountries.copy() 
eaCountries.remove("Burundi")
print(eaCountries)
print(copyCountries)


copyCountries2=[]+eaCountries
copyCountries3=[]
copyCountries3.extend(eaCountries)
