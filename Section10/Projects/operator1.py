student_names = ["Mohamed", "Ahmed", "Ali", "Sara"] 

student_grades = [[96, 78, 82, 80], [86, 92, 98, 90],  
[76, 88, 90, 72], [78, 86, 98, 88]]


#Mohamed has an average grade of 84.00 

# use for loop und use unpacking 
# use zip function() 
for student , grades in zip(student_names, student_grades):
    # print student name , grades
    print (f'Student: {student}')
    print(f'Grades')
    # use unpacking operator * and use sep= 
    #unpacking لازم اعمل  sep عشان اقدر استخدام الـ 
    print(*grades, sep=',')
    print('-'*40)

    # caluclate the average grade
    average = sum(grades) / len(grades)

    # print the average grade
    print(f'{student} has an average grade of {average:.2f}')
    print('-'*50)