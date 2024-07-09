# import library string und random 
import string
import random

# create a variable to save into capital letters , numbers und punctuation marks
characters = string.ascii_uppercase + string.digits + string.punctuation

# create a empty string 
password = ''

# ask user about length password
len_password = int(input("Enter the password length: "))

# use while loop 
while len(password) < len_password:

    # choice() >>> choice a char only and save the char in this variable 
    char_random = random.choice(characters)

    # احفظ الحروف كلها هنا 
    password += char_random

# while loop False print 
print(f"Generated Password: {password}")