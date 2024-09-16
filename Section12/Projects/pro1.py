# a dict of pizzas 
pizzas = { 
"Margherita": 120, 
"Pepperoni": 200, 
"Hawaiian": 150, 
"Meat Lovers": 250, 
"Mushroom": 140, }

# create a function to print pizzas by price
# function print_pizzas takes no parameters   
def print_pizzas():
    # use method items to print keys und values
    for pizza , price in pizzas.items():
        print(f'{pizza}: {price} EGP')

print_pizzas()
