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
        'quantity': 0,
    },
}

# 1. view available itmes and buy what he/she (er/sie) wants
# 2. view shopping cart which contains bought itmes
# 3. view the total price of the shopping cart
# 4. quit the program

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
                
            
    break