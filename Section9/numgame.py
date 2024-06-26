# import random library
import random

# winning num 
# use function randint() to create a random int
winner_num = random.randint(1 ,10)

# get number from user
num = int(input('Enter a number between 1 and 10: '))

# check if num is the winning num
if num == winner_num:
    print('You win')
else:
   print('You lost') 

