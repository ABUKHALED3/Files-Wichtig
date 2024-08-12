# هبدا لف من الـ 1 لحد 11 
#هل هو زوجي i %2 == 0 ثانيا هل قيمة الـ 
#i ضيف قيمة الـ  true 
even_numbers = [i for i in range(1, 11) if i % 2 == 0]
print(even_numbers)

# لف لحد الـ 11
#فردية i  هل قيمة 
#i to list ضيف قيمة الـ  True 
odd_numbers = [i for i in range(11) if i % 2 != 0]
print(odd_numbers)

print('-'*40)

#string ممكن اقدر استخدامو بردو مع 
fruits = ['mango', 'apple', 'kiwi', 'cherry']

#fruitاحفظ كل قيمة في متفير اسمو  fruits لف جو الـ  
#'a' فيها كلمة متكونه من حرف  fruit ثانيا بسال هل  
#list اعمل كل الحروف كبير ثم ضفها في الـ  True 
fruits_upper = [fruit.upper() for fruit in fruits if 'a' in fruit]
print(fruits_upper)


#word ثم ضيف القيمة الحالية في متفير اسمو  lsit fruits لف جو الـ 
# wordثم هنلف جو 
# وهنضيف كل حرف من الكلمة
chars = [char for word in fruits for char in word]
[print(chars)]