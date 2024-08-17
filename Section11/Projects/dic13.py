restaurant_menu = { 
"Burgers": {"Beef": 100, "Chicken": 80, "Bacon": 120}, 
"Pizzas": {"Cheese": 100, "Pepperoni": 120, "Veggie": 100}, 
"Drinks": {"Coke": 20, "Fanta": 20, "Sprite": 20}, 
"Desserts": {"Ice Cream": 50, "Chocolate Cake": 60, 
"Cheese Cake": 70}, 
"Sides": {"Fries": 30, "Onion Rings": 40, "Potato Wedges": 
50} 
} 

# chicken burger price 
print(f"Price Burgers Chicken: {restaurant_menu["Burgers"]['Chicken']} EGP")

# veggie pizza price 
print(f"Price Pizza Veggie: {restaurant_menu["Pizzas"]['Veggie']} EGP")

#chocolate cake price 
print(f"Price Dessert Chocolate Cake: {restaurant_menu["Desserts"]['Chocolate Cake']} EGP")

#Onion Rings price
print(f"Price Sides Onion Rings: {restaurant_menu["Sides"]['Onion Rings']} EGP")