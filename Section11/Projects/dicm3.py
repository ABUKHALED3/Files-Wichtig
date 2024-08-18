menu = { 
"Cheese pizza": 100, 
"Veggie pizza": 120, 
"Hawaiian pizza": 150, 
"Coke": 30, 
"Sprite": 25, 
"Fanta": 25, 
"Pepsi": 30 
} 

# a dictionary of desserts to add to the menu 
desserts = {
            'Ice Cream': 30, 
            'Chocolate Cake': 60,
            'Cheese Cake': 70,
            'Brownie': 40,
            'Donut': 30
            }

# use for loop 
# use method items.() عشان اشوف keys and value
for item , price in desserts.items():
    # add the key and value
    menu[item] = price

print(menu)