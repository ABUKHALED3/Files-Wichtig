grocery_names = ["apple", "banana", "orange", "grapes", 
"tomato", "potato", "milk", "bread", "butter"] 
grocery_prices = [0.99, 0.5, 0.75, 2.99, 1.49, 0.99, 3.99, 
2.49, 4.99] 

print('Grocery list:')
print('Item\t\tPrice')
print('-'*20)

# Loop through the list of tuples and display the grocery items and their prices 
# use zip function()
for item, price in zip(grocery_names, grocery_prices):
    print(f'{item}\t\t${price:.2f}')