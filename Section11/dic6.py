pizzas = {'Thunfisch': 140, 'Salami': 140, 
          'Chicken': 130, 'Meat Lovers': 150
        }

burgers = {'Beff': 150, 'Turkey': 110}

soups = {'Chicken soup': 40, 'Beef soup': 35, 'Mushroom soup': 40}

drinks = {'Coke': 30, 'Pepsi': 30, 'Tee': 15, 'Kaffee': 25}

desserts = {'Ice Cream': 30, 'Cake': 60} 

# dictازي اضيف ده كلو في 
new_menu = {
            'Pizzas': pizzas,
            'Burgers': burgers,
            'Soups': soups,
            'Drinks': drinks,
            'Desserts': desserts
}

#item with price عايز اطبع كل 
# use for loop

for itmes, menu in new_menu.items():
    # for loop dictتانيه عشان اخش جو كل 
    for item , price in menu.items():
        print(f'{item}: {price}EGP')