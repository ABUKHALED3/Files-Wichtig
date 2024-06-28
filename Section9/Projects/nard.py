# import radnom labrary to use function randint
import random

# random dice roll
winner_num = random.randint(1, 6)

# message to user
message = """Guess The Roll Dice!
Enter a number between 1 and 6: 
"""

# get the number from user
num_user = int(input(message))
print('-'*35)

# check user num is random num
if num_user == winner_num:
    print(f'The Dice is{num_user}\nYou Won!')
else:
    print(f'The Dice is {winner_num}\nYou lost!')