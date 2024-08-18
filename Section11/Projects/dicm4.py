menu = { 
"Cheese pizza": 100, 
"Veggie pizza": 120, 
"Hawaiian pizza": 150, 
"Coke": 30, 
"Sprite": 25, 
"Fanta": 25, 
"Pepsi": 30 
} 

# upper price to 20 prozent

# use for loop
# use method items.() to save keys und values
for item , price in menu.items():
    menu[item] = price *  1.2

print(menu)