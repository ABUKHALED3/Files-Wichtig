# a tuple of tuples
grades = (
    ('Ahmed', 95),
    ('Kemo', 75),
    ('Sara', 80),
    ('EL Sayed', 90)
)

# use for loop und enumerate function ()
# function return zewi arguments  عشان الـ  name , grade لية أنا عملت كده مع ال 
# list وممكن احطهم في  
for index , (name , grade) in enumerate(grades, 1):
    print(f'{index}. {name} got {grade} Marks')

print('-'*30)

# a list 
numbers_list = [11, 12, 54, 70]

# ([0,11]) >>> index = 0 , value = 11  
for index , value in enumerate(numbers_list):
    if value > 10:
        numbers_list[index] -= 4

print(numbers_list)
