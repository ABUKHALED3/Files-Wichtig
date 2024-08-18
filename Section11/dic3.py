# new lesson about dict
            # key      value
pizzas = {'Margherita': 100, 'Meat Lovers': 150, 'Chicken': 130}

# get from the user input
order = input('what pizza would you like: ')

# if order in pizzas 
#keys بدور حاليا في 
if order in pizzas:
    print(f'Great we have {order} pizza')
else:
    print(f"Sorry we don't have {order} pizza ")

print('-'*40)

# Methods dictعشان اقدر اشوف الـ 
print(dir(pizzas))
print('-'*40)

# values in dict
print(pizzas.values())

print('-'*40)

print(pizzas.keys())
print('-'*40)

# items.() in dict
# return tuple keys und values
for pizza , price in pizzas.items():
    print(f'{pizza}: costs {price}EGP')