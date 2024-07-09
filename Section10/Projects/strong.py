# import library random and string
import string
import random

# create a variable to save into letters , numbers und punctuation marks
characters = string.ascii_letters + string.digits + string.punctuation

# create a string variable 
password = ''

# ask user about length password
len_password = int(input('What is your length Password: '))


# use while loop 
while len(password) < len_password:

    # وهنخزنها هنا characters هتختار قيمة واحد من function choice()  بستخدم 
    char_random = random.choice(characters)

    # احفظ الحرف في المتغير ده
    password += char_random

print(f"Generated Passowrd: {password} ")