# F strings 
# {بكتب اسم المتغير هنا } ""أو '' f أكتب في الأول 
# مميزات الطريقة

#هنا لايمكن طباعة هذا  str + int 
#str من غير تحويله الي  data types و أطبع أي متغير من أي نوع function في الطريقة دي بقدر احط   

city = input("Enter your city: ") 
print(f"Your City is {city} your city is {len(city)} charaters")

num = 1000000000
print(f'The Num is {num:,}')
print(f"{50/3:.2f}")