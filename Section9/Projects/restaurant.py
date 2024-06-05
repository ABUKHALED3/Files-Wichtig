# list Pizzas in Restuarant
pizzas = ['Margherita $10',
          'Pepperoni $15 ', 
          'Super Supereme $12',
          'Hawaiia $7 ', 
          'Meat Lovers $20 ', 
          'Cheese Lovers $11', 
          'Tuna $19'
          ]

# price list pizzas 
price = [10, 15, 12, 7, 20, 11, 19]

# A message to ask the user for the pizza
message = f"""Please, Enter The number of The Pizaa you want: 
        1.{pizzas[0]}
        2.{pizzas[1]}
        3.{pizzas[2]}
        4.{pizzas[3]}
        5.{pizzas[4]}
        6.{pizzas[5]}
        7.{pizzas[6]}
"""

# get from user the order
id_pizza = int(input(f"{message}\n"))
num_pizza = int(input("Enter The number of Pizaas you want: "))

# calulate the total
total = num_pizza * price[id_pizza-1]

# print this 
print('-'*20)

# gretting the user
print("Thanks for chossing KhaLed Pizza!🍕😊\nPlease enjoy your Time")

# print the order und {pizzas[id_pizza -1 ]} >>عشان نبدا نعد من الصفر
print(f"While we get {num_pizza} pizza {pizzas[id_pizza - 1]} ready for you")

print('-'*20)

# print total
print(f"The total is ${total}")