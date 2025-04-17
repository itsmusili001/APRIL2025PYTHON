prices=[100, 200, 250,55,500]
#new_prices = []
#for price in prices:
  #  new_prices.append(int(price) *1.1)

new_prices = [price * 1.1 for price in prices]




print("old prices" + str(prices))
print("new prices" + str(new_prices))



numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sqNumbers = [x**2 for x in numbers]
print("squared numbers" + str(sqNumbers))
print("numbers" + str(numbers))

even_numbers = [x for x in numbers if x % 2 == 0]
print("even numbers: " + str(even_numbers))

odd_numbers = [x for x in numbers if x % 2 != 0]
print("odd numbers: " + str(odd_numbers))
