# id = company name + - + last 3 letters from name + birthday

company_name = "AL KhaLed-"

name = input("Enter your name: ")

birthday = input("Enter your birthdate: ")

# get from user email 
email = input("Enter your email: ")

# get last 3 letters from name
last_3_letters = name[-3:]

id = company_name + last_3_letters + birthday

#string is a list characters 
#من الحروف list عبارة عن str 
#'Hello'>> ['H', 'e', 'l', 'l', 'o']

# method index search for a value in string and return number index
index_at = email.index("@")

#edited email
new_email = email[ :index_at] + "@alkhaled.com"

print("-"*20)

print(f"Your id is {id}")
print(f"Your email is {new_email}")
