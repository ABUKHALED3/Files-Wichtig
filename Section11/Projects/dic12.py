students = { 
    "Mohamed": {"grades": { 
        "math": 100, 
        "english": 90, 
        "science": 80, 
        "arabic": 100,  
        "history": 97}, 
        "school": "Codezilla" 
    }, 
    "Ahmed": {"grades": { 
        "math": 100, 
        "english": 95, 
        "science": 93, 
        "arabic": 100, 
        "history": 94}, 
        "school": "Codezilla" 
    }, 
 
 
 
    "Ali": {"grades": { 
        "math": 85, 
        "english": 83, 
        "science": 87, 
        "arabic": 100, 
        "history": 90}, 
        "school": "Al-Azhar" 
    }, 
    "Sara": {"grades": { 
        "math": 100, 
        "english": 94, 
        "science": 98, 
        "arabic": 100, 
        "history": 100}, 
        "school": "Al-Azhar" 
    } 
} 
print(students['Mohamed']['grades']['math'])
print(students['Mohamed']['grades']['english'])
print(students['Mohamed']['school'])

print('-'*50)

# Ahmed grades in math, science, and Arabic 
print(students['Ahmed']['grades']['math'])
print(students['Ahmed']['grades']['science'])
print(students['Ahmed']['grades']['arabic'])

print('-'*50)
# Ali school and grades in history, science, and Arabic 

print(students['Ali']['grades']['history'])
print(students['Ali']['grades']['science'])
print(students['Ali']['grades']['arabic'])

print('-'*50)

# Sara grades in math, science, and history 
sara_grades = students["Sara"]['grades']
print(sara_grades['math'])
print(sara_grades['science'])
print(sara_grades['history'])

