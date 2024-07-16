# a list of prices for different items in dollars

prices = [10.99, 9.99, 15.99, 7.99, 12.99]

sum = 0.0

#count بستخدم متغير اسمو  List عشان الف جو الـ  for loop هستخدم 
for price in prices:
    # priceمع الـ sum قيمة الـ  
     sum += price


print(f'The total cost is {sum} dollars')
