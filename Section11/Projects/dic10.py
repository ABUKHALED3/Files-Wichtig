# Available Pizzas: 
pizzas = {
            #Key >>> Value
            "Margherita": 100,
           "Pepperoni": 120, 
           "Meat Lovers": 150, 
            "Chicken": 130
}

# for loop through the pizzas dictionary
for pizza in pizzas:
    # print the name of pizza und the price
    print(f'{pizza} price: {pizzas[pizza]}EGP')