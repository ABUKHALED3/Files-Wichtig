# A dictinoary of available items

available_items = {
    'Iphone 12':{
        'price': 22000,
        'quantity': 4,
    },

    'Iphone 12 Pro':{
        'price': 24000,
        'quantity': 4,
    },

    'Iphone 12 Pro Max':{
        'price': 25500,
        'quantity': 7,
    },

     'Iphone 13 ':{
        'price': 26500,
        'quantity': 7,
    },
     'Iphone 13 Pro ':{
        'price': 27000,
        'quantity': 7,
    },
     'Iphone 13 Pro Max':{
        'price': 29500,
        'quantity': 7,
    },

    'Iphone 14 ':{
        'price': 33000,
        'quantity': 1,
    },
}

# intialize the shopping cart as dict
cart = {}

menu_message = """
What would you like to do?
1. View available itmes
2. View Cart
3. View total price of cart
4. Quit
"""


# use while loop until user input quit
while True:

    print(menu_message)

    # get the user's choice
    user_choice = input('Enter your choice: ') 

    # 1. if the user chose to view available items
    if user_choice == '1':
        print('The Available itmes are: ')

        # use function enumerate 
        # index عشان 
        # enumerate  return index and key 
        for i, item in enumerate(available_items):

            # make a varaible to save into the quantity
            item_quantity = available_items[item]['quantity']

            # if item True نفذ اللي تحت
            # Trueاحنا قولنا اي قيمة غير الصفر 
            # check if item is not available  
            if item_quantity:
                print(f'{i+1}. {item} Price {available_items[item]['price']} EGP')
            
            else:
                print(f'{i+1}. {item} Price {available_items[item]['price']} EGP (out of stock)')    
    
        
        # get the item the user wants to buy
        order_number = int(input('Enter the number of the item you want to buy (Enter 0 to return the menu): '))
        
        # if user chose 0 
        if order_number == 0:     
            # أبدا اللوب تاني من الأول
            continue
        

        # get the item name from the item number
        # use method keys to return keys und save it as list

        # item_name[item_number - 1]
        order_name = list(available_items.keys())[order_number - 1]

        # check if item is not available (quantity 0 )
        available_quantity = available_items[order_name]['quantity']
        if available_quantity == 0:
            print('Sorry the item is out of stock')

            # key word continue 
            # تجاهل الكود اللي تحت ده وعيد اللوب من الاول
            # تخرج من اللوب break عكس الـ  
            continue

        # subtract 1 from the quantity
        # نقص واحد من الكمية
        available_items[order_name]['quantity'] -= 1

        # add the bought item to the cart 

        # get the price of the bought item
        order_price = available_items[order_name]['price']

        # get the quantity of the bought item
        # use get method to solve this
        order_quantity = cart.get(order_name, {}).get('quantity', 0) + 1

        # save order info
        order_info = {
            order_name: { 
            'price': order_price,
            'quantity': order_quantity
            }
        }

        # add order info to the cart 
        cart.update(order_info)

        # confirm that the order has been added to the cart
        print(f'{order_name} has been added to the cart successfully')

    # if user chose 2 view cart
    elif user_choice == '2':
        if cart: 
            print('\nCart')

            # use for loop through cart dict
            for item in cart:
                # Value هات الـ 
                item_price = cart[item]['price']
                item_quantity = cart[item]['quantity']
                print(f'{item}: {item_price:,} EGP x {item_quantity}')

            # else if the cart empty >> False 
        else: 
            print('Your Cart is Empty!')

        # عشان لما المستخدم يختار 2 نعرض لها اجمالي السعر    
        # a list to store the total price each item in the cart
        # 1 loop through cart
        # 2 get the price of each item 
        # 3 get the quantity of each item
        # 4 الضرب
        lst_total_item_price = [cart[item]['price'] * cart[item]['quantity'] for item in cart]


        # sum all the items in the cart to get the total price
        total_price_cart = sum(lst_total_item_price)
        print(f'Total Price Of Cart {total_price_cart:,} EGP')

    # if user chose 3 
    elif user_choice == '3':
        lst_total_item_price = [cart[item]['price'] * cart[item]['quantity'] for item in cart]

        # sum all the items in the cart to get the total price
        total_price_cart = sum(lst_total_item_price)
        print(f'Total Price Of Cart {total_price_cart:,} EGP')

    # if user chose 4
    elif user_choice == '4':
        print('Thanks for shopping at Khaledit Store🥳')
        # break out of the loop
        break
    
    # if user chose an invalid option
    else:
        print('Please enter a number between 1 and 4.')
        
# if cart items print the cart
if cart:
    print('\nCart')

    # use for loop through cart dict
    for item in cart:
        # Value هات الـ 
        item_price = cart[item]['price']
        item_quantity = cart[item]['quantity']
        print(f'{item}: {item_price:,} EGP x {item_quantity}')

# else if the cart empty >> False 
else:
    print('Your Cart is Empty!')


# a list to store the total price each item in the cart
# 1 loop through cart
# 2 get the price of each item 
# 3 get the quantity of each item
# 4 الضرب
lst_total_item_price = [cart[item]['price'] * cart[item]['quantity'] for item in cart]


# sum all the items in the cart to get the total price
total_price_cart = sum(lst_total_item_price)
print(f'Total Price Of Cart {total_price_cart:,} EGP')