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

# mohamed hassan's total 93% prozent

# for loop عشان الف جو هنا
for student in students:
    grades = students[student]['grades']

    total = sum(grades.values()) / len(grades)    

    print(f'{student.title()} total {total}% Prozent')

    print('-'*20)