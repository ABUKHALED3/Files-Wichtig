drinks = { 
"Coke": 30, 
"Sprite": 25, 
"Fanta": 25, 
"Pepsi": 30, 
"Tea": 20, 
"Coffee": 25, 
"Orange Juice": 30, 
"Mango Juice": 30 
} 


# a list of drinks to print
drinks_print = ['Coke', 'Mango Juice', 'Tea', 'Coffee']

# use for loop 
for drink in drinks_print:
    print(f'{drink}: costs {drinks[drink]}')