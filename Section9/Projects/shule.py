# A list of students ids
students = [
            #Codezila school
            ['1100','1101','1102','1103','1104'
             ,'1105''1106','1107','1108','1109',],
             
             # Al Dorra school
             ['2100','2101','2102','2103','2104',
              '2105','2016','2017','2018','2019'],
            
            # Mostafa Kamel School
            ['3100','3101','3102','3103','3104',
             '3105','3106','3107','3108','3109'],
] 

# input id Students
students_id = input("Enter Student id: ")

# Check students id in list Students
if students_id in students[0]:
    print("Student is in Codezilla School")
elif students_id in students[1]:
    print("Student is in AL Dorra School")
elif students_id in students[2]:
    print("Student is in Mostafa Kamel School")
else:
    print("Sorry, Student is not in our records")