# create a strong password using numbers , letter und puctuation marks 

# import library string , random to use it  
import string
import random

# create a variable to save into letters, numbers und punctuation marks 
characters = string.ascii_letters + string.digits + string.punctuation 

# password length عدد حروف الباسورد 
password_len = 15

# make a variable to save into random password
password = ''

# use while loop 
while len(password) < password_len:

# use function choice() in library random to choice a random char
#  عشان حرف واحد عشوائي و خزنتو في متغير  function choice() in library random أستخدامت 
    random_char = random.choice(characters)
    
    # password علي قيمة  random_char حط قيمة  
    password += random_char


# when while loop False print the generated password
print(password)