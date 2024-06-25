# Employees and their offices
cairo = ['Islam Mahfouz', 'Mohamed Mesilhy', 
'Hatem Elmaghraby', 'Kareem Embaby']

riyadh = ['Mohamed Gouda', 'Ayman Hamed', 
'Seif Ali', 'Adham Wael']

casablanca = ['Ahmed Ashraf', 'Abd El-Rahman Mahrous', 
'Islam Sheta', 'Mohamed Medhat', 'Mahmoud Nasser']

dubai= ['Ahmed Alaa', 'Kareem Abd-Elmeged', 
'Osama Ashraf', 'Mohamed Mostafa', 'Ahmed Bedeir']

# get the name of the office 
office = input('Enter the name of the office: ').lower()

# check use match
match office:
    case 'cairo' | 'egypt':
        employess = cairo
    
    case 'riyadh' | 'saudi arabia' | 'ksa':
        employess = riyadh
    
    case 'casablanca' | 'morocco':
        employess = casablanca
    
    case 'dubai' | 'uae':
        employess = dubai
    
    case _:
        employess = False
        print('Not Found')

if employess:
    # make a string of the employess
    employess_str = ', '.join(employess[:-1]) + ' and ' + employess[-1]

# print the employess
    print(f'The employess in {office.upper()} are: {employess_str}.')