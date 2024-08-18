pizzas = { 
        "Margherita": 100,  
        "Pepperoni": 120,  
        "Meat Lovers": 150,  
        "Chicken": 130, 
        "Cheese": 100, 
        "Veggie": 120, 
        "Hawaiian": 150, 
        } 

# use for loop عشان الف جو 
# use method items.()
# use unpacking in a variable
for pizza , price in pizzas.items():
    if pizza == 'Pepperoni' or pizza == 'Chicken' or pizza == 'Hawaiian':
        print(f'{pizza} costs {price}')