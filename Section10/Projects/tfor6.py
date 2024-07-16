# a list of prices 
prices = [10.99, 20.99, 30.99, 40.99, 50.99] 

# Initalizl empty list 
str_prices = []

#list prices عشان الف جو  for loop هستخدم 
for price in prices:
    # convert int >> str mit $ and save it in the new variable
    price_dollar = str(price) + '$'

    # add the each price in the list 
    str_prices.append(price_dollar)

# print list str prices
print(str_prices)
