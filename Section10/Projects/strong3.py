# import library string und random 
import string
import random

# create a variable to save into letters , numbers , punctuation 
characters = string.ascii_letters + string.digits + string.punctuation

# create a empty list
password = []

# ask user about the length password 
len_password = int(input('Enter the password length: '))

# 
letter_count = len_password // 2 + len_password % 2

# Add the letters to the password 
i = 0 
while i < letter_count: 
    password.append(random.choice(string.ascii_letters))
    i+= 1


# use while loop 
while len(password) < len_password:

    # choice() >>> choice a char random and save this char into variable
    # append this char in list password
    password.append(random.choice(characters))


# بتغير الاماكن
random.shuffle(password)

# convert the password to a string 
password = ''.join(password)


print(f"Generated Password: {password}")
 