numbers = [-588, -479, -713, -701, -885, -578, -835, -466, 
-935, -665, -360, -837, -389, -367, -454, -668, -907, -822, 
-541, -680, -405, -330, -625, -916, -331, -876, -689, -753, 
-810, -648, -787, -952, -718, -401, -502, -699, -533, -450, 
-580, -725] 

smallest = numbers[0]

# loop through the list of number
for i in numbers:

    # cehck if 
    # هل الرقم ده أقل من الرقم اللي هو جو المتغير
    if smallest < i:
        # update the value in number
        # I غير قيمة المتفير الي قيمة الـ 
        smallest = i 

# print the smallest number
print(f'The smallest number is {smallest}')