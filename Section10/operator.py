# lesson about unpacking operator und print function()

# a list of numbers 
numbers = [1,2,3,4,5,6]

# a Tuple 
name = 'Ahmed' , 'KhaLed'
# print function() takes one argument أجباري والباقي اختياري
# sep ist keyword in print function تفصل بينهم بي مسافة 
# unpacking لما نحط النجمه دي * بعمل  
# لازم احط النجمة قبل المتغير
print(*name, sep='1')

#  لما نحط النجمه دي * بعمل  
# لازم احط النجمة قبل المتغير
#  لازم اعمل  sep عشان اقدر استخدام الـ  
print(*numbers, sep ='-')

print('-'*50)

# unpacking operator مثال أخر علي 

scores = [70, 88, 90, 74, 92, 95]

# النجمة تعني انها تاخذ كل القيمة ماعدا القيمة الأخيرة عشان في متغير هياخذها
first , *rest, last = scores
print(first, rest, last)