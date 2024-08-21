pharmacy_prices = {
    'panadol': 40,
    'cold free': 30,
    'omega 3': 50
}

# get from user input
user_input = input('Enter the item to search for: ')

# use method seatdefault.()
#Noneتضيفو وتضيف قيمتو  key لو ملقتشي الـ   key بتدور علي الـ  

# takes zwei arguments
# eins ist a key 
#اختياري key قيمة الـ  zwei 
item_price = pharmacy_prices.setdefault(user_input)

print(f'{user_input}: {item_price}')
print(pharmacy_prices)