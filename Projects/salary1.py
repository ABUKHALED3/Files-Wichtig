# get name user , remove extra spaces und capital first letter each word
name = input("Name: ").strip().title() 

# get currency , remove extra spaces und capital first leeter each word
currency = input('Currency: ').strip().title()

# get number of Hours und convert str >>> float 
num_uhr = float(input('Number of Hours: '))

# get Hourly Rate und use function float 
# convert str >>> folat
rate = float(input("Hourly Rate: "))

# salary
salary = num_uhr * rate

# print salary 
print(f"The Salary of {name} is {salary:,} {currency}")