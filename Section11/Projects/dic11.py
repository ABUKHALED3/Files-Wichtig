students = { 
"Mohamed": {"grades": [100, 90, 80], "age": 20}, 
"Ahmed": {"grades": [100, 95, 93], "age": 21}, 
"Ali": {"grades": [85, 83, 87], "age": 19}, 
"Sara": {"grades": [100, 94, 98], "age": 21} 
} 

print(students["Mohamed"]["grades"]) 
print(students["Ali"]["age"])

sara_grades = students["Sara"]['grades']
print(*sara_grades, sep = '\n')