# id = first 3 characters of company name + - + last 2 characters of name + birth year

# get data from user
company_name = input("Enter your company name: ").strip().title()
name = input("Enter your name: ").strip().title()

birth_year = input("Enter your birth year: ")
email = input("Enter your email: ")

# first 3 characters of company name
letters_of_company = company_name[:3]

# last 2 characters of name
last_letters_of_name = name[-2:] 
idx_name = name.index(" ")

# new id from user
new_id = letters_of_company + "-" + last_letters_of_name + birth_year

# new email 
idx_email = email.index("@")
new_email = email[:idx_email] +  f"@{company_name}.com"


print("-"*20)

# greet the user
print(f"Hello, {name[:idx_name]}!\nWelcome at {company_name}!")

print("-"*20)

# print id form user
print(f"Your id is: {new_id}")

# print email from user
print(f"Your eamil is: {new_email}")
