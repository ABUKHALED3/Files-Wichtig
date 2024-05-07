# get name user , remove spaces und cpaital letter of first word
name = input("Enter Your Name: ").strip().lower()

# get birth year from user
year = input("Enter Your Birth Year: ")

# get birth month from user
month = input("Enter Your Birth Month: ")

# get birth day from user 
day = input("Enter Your Birth Day: ")

#rplace " " to _
username = name.replace(' ','_')

# username 
username = f'{username}_{day}_{month}_{int(year) + (len(name))}' 

# print
print("-"*40)

print(f"Hello, {name}\nYour username is ...\n{username}@codezilla.com")
