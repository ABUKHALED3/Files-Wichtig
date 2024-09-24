
# use funtion open to open the file
# بكتب اسم الملف زي ما هو كده 
#f وخزنتو في متغير اسمه 
f = open('employess_data.txt')

#print(f.read())


#print(f.readline())

emps_data = f.readlines()

for employee in emps_data:
    emp = employee.strip().split('-')
    salary = float(emp[-1]) * 2

    print(f'{emp[0]} - {emp[1]}- {salary}')

#عشان البرنامج ميهنجشي  Close  زي ما فتحت الملف لازم اعمله 
f.close()

with open('employess_new_data.txt','w') as f :
    for employee in emps_data:
        emp = employee.strip().split('-')
        salary = float(emp[-1]) * 2

        f.write(f'{emp[0]} - {emp[1]}- {salary}\n')


