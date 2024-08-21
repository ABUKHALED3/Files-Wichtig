# a dict
pharmacy_prices = {
    'panadol': 32,
    'cold free': 20,
    'omega 3': 45,
    'fuciden': 40
    }

# get from the user input
user_input = input('Enter the item to search for: ')

# use get.() 
# get takes zewi arguments 
# Eins ist a key  الحاجة اللي انت بتدور عليها 
# zewi ist لو محددتش None اختياري و بيطلع

item_price = pharmacy_prices.get(user_input, 'Not avaliable')

print(f'{user_input}:  {item_price}')