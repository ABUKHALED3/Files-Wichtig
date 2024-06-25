# Employees and thier offices
cairo = ['Ahmed Khaled', 'Hesham Amr', 'Amgad Mahfouz']
riyadh = ['Seif Ali', 'Mostfa Hamdy', 'Zyead Weal']
prague = ['Osama Ashraf', 'Zakria Elsayed','Mohamed Essam']
dubai= ['Kareem Ayman', 'Abdo Kamel', 'Emad Samy']

# get office name
office = input('Enter the name of the office: ').lower()

# use match for check
# how to write match  معني|>> or 
match office:
    case 'cairo' | 'egypt':
        print(cairo)
    case 'riyadh'| 'ksa' | 'saudi':
        print(riyadh)
    case 'prague' | 'czech':
        print(prague)
    case 'dubai'| 'uae':
        print(dubai)
    # else 
    case _:
        print('Not Found')