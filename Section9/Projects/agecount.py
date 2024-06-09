# get data from user about name, birth date, Current year

name = input("Enter your full name: ")
birth_date = (input("Enter your birth date (dd-mm-yyyy): "))
year = int(input("Enter the current year: "))

# first name 
first_name = name.split()[0]

# get year
list_birth_date = birth_date.split("-")
#convert str to int 
year_date = int(list_birth_date[2])

# Age Calculator
age = year - year_date

print("-"*60)
print(f"Hello, {first_name.title()}\nWelcome at Age Calulator")
print("-"*60)

print(f"Your age is {age}")