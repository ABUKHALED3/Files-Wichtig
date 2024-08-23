items = {
    'panadol': 
    {
    'price': 32,
    'quantity': 10,
    },

    'cold free':
    {
    'price': 37,
    'quantity': 10, 
    },

    'omega 3 ':
    {
    'prcie': 45,
    'quantity': 7,
    },

    'fuciden':
    {
    'price': 30,
    'quantity': 4 
    }
}


# get from user input
user_input = input('Enter item name: ')

# use get.() method
# return a value 
#وعشان ميحصلشي خطاء dictتتعمل مع الـ  getعشان الـ  dict حطيت هنا 

# price اللي المستخدم ادخله هتالي قيمة الـ 
#  لو مش موجود رجع 
details = items.get(user_input, {}).get('price', 'Not available')

print(details)