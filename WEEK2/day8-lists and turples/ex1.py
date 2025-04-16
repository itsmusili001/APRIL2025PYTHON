friends= ["ann","john","peter","clark","fred","nancy","Mary"]
fruits=list(("kiwi","oranges","Bananas","mangoes"))
prices=[34.99,500.0,45.89]

#print(friends[3])
#print(fruits[0])

for friend in friends:
    print(friend)
total=0
for price in prices:
    total=total+price

print (f"total price: kshs{total:.2f}")

print(f"total price: kshs {sum(prices):.2f}")

