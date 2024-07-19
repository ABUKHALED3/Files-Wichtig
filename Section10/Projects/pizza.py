# a list of pizzas 
pizzas = ['Margherita', 'Pepperoni', 'Super Supreme', 
'Hawaiian', 'Meat Lovers', 'Cheese Lovers'] 

# drei prints in user 
print('Welcome to Codezillas Pizza!')
print('We have the following Pizzas:')
print('-'*50)

# print the pizzas to user  
for i in range(len(pizzas)):
    print(f'{i + 1}. {pizzas[i]}')

# ask user about the number pizza you want
user_order = int(input('Enter the number of the pizza you want to order: ')) 

# ask user about the number of pizzas want
numbers_pizzas = int(input('Enter the number of pizzas you want: '))

print('-'*45)
print('Thanks for choosing Codezillas Pizza!\nPlease, Enjoy your time')
print(f'While we get {numbers_pizzas} {pizzas[user_order - 1]} Pizza ready for you')