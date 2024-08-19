students = { 
    "Mohamed Hassan": {"grades": { 
        "math": 100, 
        "english": 90, 
        "science": 80, 
        "arabic": 100,  
        "history": 97} 
    }, 
    "Ahmed Kamal": {"grades": { 
        "math": 100, 
        "english": 95, 
        "science": 93, 
        "arabic": 100, 
        "history": 94} 
    }, 
    "Ali Adel": {"grades": { 
        "math": 85, 
        "english": 83, 
        "science": 87, 
        "arabic": 100, 
        "history": 90} 
    }, 
    "Israa Ali": {"grades": { 
        "math": 100, 
        "english": 94, 
        "science": 98, 
        "arabic": 100, 
        "history": 100} 
    } 
} 



# get from the user name student
name = input('Please, Enter the name of the student: ').title()

# use for loop عشان اللف
if name in students:

    # save the subjects and grades
    grades = students[name]['grades']
    
    # print this form user
    print(f'{name} got the following grades: ')

    # use for loop and item.() method
    for subject , grade in grades.items():

        # print the subject und grade
        print(f'{subject.title()}: {grade}')

        # حساب النسبة المئوية
        total = sum(grades.values()) / len(grades)

    print('-'*20)
    print(f'{name} total prozent is {total}')
    
else:
    print('Sorry we dont have info about this student')