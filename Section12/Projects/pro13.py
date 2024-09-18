import random
import string
def random_pass(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

print(f'Password Generated: {random_pass()}')
        
