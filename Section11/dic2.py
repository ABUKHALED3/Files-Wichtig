# More lernen about Dic
            # Key     Value
# : ist a key >>> value 
# : value بعد العلامة دي 
students = {'Ahmed':{'grades':[100, 85, 90],'age': 21},
            'Ali' :{'grades':[99, 87, 69], 'age': 22},
            'Hesham':{'grades':[83, 77, 99], 'age': 19}
            }
#value طريقة الوصول الي اي 
print(students['Ahmed']['grades'][0])
print(students['Ali']['grades'])
print(students['Ahmed']['age'])

print('-'*40)

# save the grades in avarible
ahmed_grades =(students['Ahmed']['grades'])

# caluclate the average grades
average = sum(ahmed_grades) / len(ahmed_grades)

print(f'The average ist {average:.2f}')