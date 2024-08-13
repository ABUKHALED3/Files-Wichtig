# Die Lektion about Dictionaries

#Dictionarie ازي اكتب 
# {} اللي انا عايزو ثاني  Dictionarie بكتب اسم الـ  zuerst

pizass = {
        # key word >>>>  value
        'Meat Lovers' : 170,
        'Margherita' : 160,
        'Chicken' : 145,
        'hamada' : 1000
    }
#key word زي ما هي كده عشان اقدر اطبع القيمة اللي شيلها key word بكتب اسم الـ 
print(pizass['Margherita'])
print('-'*40)
print(pizass['hamada'])

#Dictionaries طريقة الأضافة في 
#Dictionarie بكتب اسم الـ 
# ثم الحاجة اللي عايز اضفها 
pizass['Pepperoni'] = 120
print(pizass)

print('-'*40)
#value طريقة التعديل في 
#key word بكتب اسم الـ 
pizass['Meat Lovers'] = 175
print(pizass)

print('-'*40)

# طريقة المسح 
#key wordثم  Dictionarieثم اسم  del بكتب 

#Dictionarie وممكن امسح الـ 
# del pizzas

del pizass['hamada']
print(pizass)
print('-'*40)

# data types ممكن يكون اي نوع values
#int - str - tuple - bool - float  ممكن يبقا key words
test = {
    1 : True,
    'average': 12.5,
    ('grades' ,'scores') : 90,
     False : 'Ahmed'
}
print(test[1])