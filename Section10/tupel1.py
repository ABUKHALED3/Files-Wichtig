# Neu lektion about Tupels 

# wie schreibst du Tupels ? 
# Tupels ازي اكتب الـ 

# , تكتب بي () أو من غير الأقواس لكن يلزم كوم 

numbers = 1, 2, 3, 4, [1,0]
numbers1 = ('a', 'Hallo', 1.5 , True)

print(type(numbers))
print(type(numbers1))

print('-'*30)

# , يلزم الكوم  Tupels أزي أكتب قيمة واحده جوه الـ 
char = 'a',
print(type(char))

# مهم جدا في تبديل القيمة ببعضTupels 
a = 20
b = 10

print(a, b)

a , b =  b , a
print(a, b)

print('-'*40)

# Tupels wchtig in unpack 
# تفريغ البيانات جو متفيرات بترتيب
personal_details = ('Ahmed', 21, 1245765)

name, age, telefon = personal_details

print(name, age , telefon)