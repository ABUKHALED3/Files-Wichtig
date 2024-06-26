# import random library
import random

# winning nummers 
# use function randint() to creat a random int 
winner1 = random.randint(1 ,20)
winner2 = random.randint(1, 20)  
winner3 = random.randint(1, 20)  
winner4 = random.randint(1, 20)  

# list of winning numbers 
winners = [winner1, winner2, winner3, winner4]

# get number for user
num_user = int(input('Enter the number between 1 and 20: '))

# check if num user is winning numbers
if num_user in winners:
    print('You win')
else:
    print('You lost') 