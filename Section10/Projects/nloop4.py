numbers = [-588, -479, -713, -701, -885, -578, -835, -466, -935, -665, -360, 
-837, -389, -367, -454, -668, -907, -822, -541, -680, -405, -330, 
-625, -916, -331, -876, -689, -753, -810, -648, -787, -952, -718, 
-401, -502, -699, -533, -450, -580, -725]

# initial the largest number  
largest = numbers[0]

# use for loop
for num in numbers:
    # check if
    # هل الرقم ده اكبر من الرقم ده و يقبل القسمة علي 2
    if num > largest and num % 2 == 0 :
        largest = num

# print the num
print(f'The largest even number is {largest}')

# anthoer Soultion

# initial the largest even number  
for number in numbers:
    # check if the number is even 
    if number % 2 == 0:
        largest_even = number
        # break out of the loop
        break

# loop through the list 
for number in numbers:
    # check if the number is even and largest even أكبر من 
    if number % 2 == 0 and number > largest_even:
        largest_even = number

print(f'The largest even number is {largest_even}')
