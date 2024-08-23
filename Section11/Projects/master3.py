products = { 
"T-shirt": {"price": 300, "quantity": 10}, 
"Shirt": {"price": 250, "quantity": 20}, 
"Pants": {"price": 300, "quantity": 15}, 
"Shoes": {"price": 400, "quantity": 5}, 
"Socks": {"price": 25, "quantity": 7}, 
"Hat": {"price": 50, "quantity": 8}, 
"Gloves": {"price": 50, "quantity": 10}, 
"Sweater": {"price": 500, "quantity": 20}, 
"Jacket": {"price": 900, "quantity": 15}, 
"Coat": {"price": 1000, "quantity": 5}, 
"Scarf": {"price": 110, "quantity": 2}, 
} 

# use while loop
while True:
    user_input = input('Enter the product name (Press Enter to Exit): ').title()

    if user_input == '':
        print('Thanks for Choosing Codezilla')
        break

    # use get method to show value
    #und not available  {} لو القيمة مش موجوده رجع الـ 
    # get price of items
    price = products.get(user_input, {}).get('price', 'Not Available')
    
    # get quantity
    quantity = products.get(user_input, {}).get('quantity', 'Not Available')

    message = f"""Product: {user_input}
Price: {price}
Quantity: {quantity} 
"""
    print(message)