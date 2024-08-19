students = { 
    "Mohamed Hassan": {"grades": { 
        "math": 100, 
        "english": 90, 
        "science": 80, 
        "arabic": 100,  
        "history": 97}, 
        "school": "Codezilla" 
    }, 
    "Ahmed Kamal": {"grades": { 
        "math": 100, 
        "english": 95, 
        "science": 93, 
        "arabic": 100, 
        "history": 94}, 
        "school": "Codezilla" 
    }, 
    "Ali Adel": {"grades": { 
        "math": 85, 
        "english": 83, 
        "science": 87, 
        "arabic": 100, 
        "history": 90}, 
        "school": "Al-Azhar" 
    }, 
    "Sara Ahmed": {"grades": { 
        "math": 100, 
        "english": 94, 
        "science": 98, 
        "arabic": 100, 
        "history": 100}, 
        "school": "Al-Azhar" 
    } 
} 

# use for loop 
for student in students:
    # save the name school in a varaible
    school = students[student]['school']
    # save grades value in a varaible
    grades = students[student]['grades']
    
    # print name
    print(f'Student Name: {student}')
    # print name school
    print(f'School: {school}')

    print('Grades:')

    # use method items.() Kyes und values
    # use unpacking
    for subject , grade in grades.items(): 
        # print اسم المادة و الدرجة
        print(f'{subject.title()}: {grade}')
    
    print('-'*25)
