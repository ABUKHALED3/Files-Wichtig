pizzas = {'Margherita': 100, 
          'Pepperoni': 120,
          'Meat Lovers': 170,
          'Chicken': 140,
          }

# add a key and vlaue
pizzas['Ranch'] = 180

# update.() 
# dict بتضيف قيمة جديده لي الـ  
pizzas.update({'Salami': 140, 'Thunficsh': 120})
print(pizzas)

print('-'*20)

# a new dict
burgers = {'Beef': 100, 'Turkey': 120}
pizzas.update(burgers)

new_menu = pizzas.copy()

# use del or clear.() to del the dict
del pizzas

# new lists 
drinks = ['Coke', 'Sprite', 'Pepsi']

price = [30, 25, 31]

# use zip function 
# use dict 
#dict عشان اضفهم الي الـ 
drinks_dict = dict(zip(drinks, price))

new_menu.update(drinks_dict)

# طريقة تاني الي الأضافة
# keys and vlaues ** عشان افضي 
#new_menu = {**new_menu, **drinks_dict}

print(new_menu)