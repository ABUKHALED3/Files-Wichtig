# import random library
import random

# winner num 
winner = random.randint(1, 2)

# form user
message = """Guess the coin flip!
Enter
1 for Heads
2 for Tails
"""

# get the number from user
num_user = int(input(message))
print('-'*30)

# check if num user is winner
if winner == 1:
    print('The Coin is Heads')
else:
    print('The Coin is Tails')

# check if the user correctly

if num_user == winner:
    print('You Win')
else:
    print('You lost')