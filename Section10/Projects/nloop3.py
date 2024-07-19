numbers = [-588, -479, -713, -701, -885, -578, -835, -466, -935, -665, -360, 
-837, -389, -367, -454, -668, -907, -822, -541, -680, -405, -330, 
-625, -916, -331, -876, -689, -753, -810, -648, -787, -952, -718, 
-401, -502, -699, -533, -450, -580, -725]

# initialize the largest number
largest = numbers [0] 

# loop in list numbers 
for num in numbers:
    # check if the number 
    # هل الرقم ده أكبر من ده
    if num > largest:
       # update the largest number 
       largest = num

print(f'The largest number is {largest}')