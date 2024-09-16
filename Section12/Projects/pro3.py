def print_students_info(name, age, city ="Cairo", school="Codezilla"): 
    print(f"Name: {name.title()}") 
    print(f"Age: {age}") 
    print(f"City: {city.title()}") 
    print(f"School: {school.title()}\n")


print_students_info('ahmed Mohamed', 25)

print_students_info('mohamed Ahmed',33, school='Al-Azhar')

print_students_info('ali Hassan', 30, city='Alexandria')

print_students_info('ahmed khaled', 22, city='Berlin', school="Khaled ibn al-Walid" )

print_students_info('hamed ali', 25, city='Tanta', school='Al Durra')