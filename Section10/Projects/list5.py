nums = [2, 29, 4, 8, 42, 55, 70, 74, 78, 27] 

#list nums لف جو الـ 
#num ثم ضيف كل قيمة في متفير اسمو 
# هل هو رقم زوجي 
#num ضيف قيمة الـ True 
#sum function ثم استخدامنا 
sum_even = sum([num for num in nums if num %2 == 0 ])
print(sum_even)