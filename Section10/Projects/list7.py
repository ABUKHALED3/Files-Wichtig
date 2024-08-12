"""Write code to find the sum of numbers that are divisible by 3 
and between 20 and 140 then print the numbers separated by a 
comma"""

# أبدا لف من 20 لحد 140
#num ثم خزن كل قيمة في متفير اسمو 
#يقبل القسمة علي 3  num  هل الـ 
#functionضيف هذا الرقم ثم استخدمنا sum  true 
by_3 = ([num for num in range(20 , 141) if num % 3 == 0])

total = sum(by_3)
print(by_3)

# convert the numbers to strings 
numbers = [str(num)  for num in range (20, 141) if num % 3 == 0] 

print(f"The numbers are {', '.join(numbers)}.") 
print(*by_3, sep=", ") 