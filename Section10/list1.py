# import libaray random
import random

# create a empty list to save into the numbers
numbers = []

# use for loop عشان اللف عشرة مرات
for i in range(1, 11):
    #i to list ضيف قيمة الـ 
    numbers.append(i)

print(numbers)

print('-'*40)

# lesson about list Comprehension
# for loop or if أكتب جوها الـ
#i to list  ضيف قيمة الـ 
new_numbers = [i for i in range(1, 11)] 
print(new_numbers)

