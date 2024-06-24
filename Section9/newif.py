# Employees and thier offices
cairo = ['Ahmed Khaled', 'Hesham Amr', 'Amgad Mahfouz']
riyadh = ['Seif Ali', 'Mostfa Hamdy', 'Zyead Weal']
prague = ['Osama Ashraf', 'Zakria Elsayed','Mohamed Essam']
dubai= ['Kareem Ayman', 'Abdo Kamel', 'Emad Samy']

# get the name of employee
name = input('Enter the name of the employee: ').title()

# check employee's office
if name in cairo:
    office = 'Cario'
elif name in riyadh:
    office = 'Riyadh'
elif name in prague:
    office = 'Prague'
elif name in dubai:
    office = 'Dubai'
else:
    office = False
    print('The employee is not found')

# print the office
# truthy values - falsy values
# falsy اي متغير قمته فاضي تبقا 
# truthy اي متغير مخزن قيمة يبقا 
if office:
    print(f'{name} works in {office} office')