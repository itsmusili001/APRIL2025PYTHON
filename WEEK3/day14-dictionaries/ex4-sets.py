# a set does not use key-vale pairs like a dictionary
# a set is no orderly
fruits = {"oranges", "lemons", "apples"}
fruits2=set(["avocados", "pineapples","lemons"])
fruits3=set() # creating an empty set
fruits3=fruits.union(fruits2) 
print(fruits3)

# adding an item to a set
fruits3.add("kiwi") 
print(fruits3)

# intersection of two sets
fruits3=fruits.intersection(fruits2) 
print(fruits3)

