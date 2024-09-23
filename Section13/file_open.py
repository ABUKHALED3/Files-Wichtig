
# use funtion open to open the file
# بكتب اسم الملف زي ما هو كده 
#f وخزنتو في متغير اسمه 
f = open('employess_data.txt')

#print(f.read())


#print(f.readline())

emps_data = f.readlines()

for employee in emps_data:
    print(employee)