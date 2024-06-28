# import random library to use radnint()
import random

# import time library to use time()
import time
   

# list of words
words = [ 'hallo', 'there','geld', 'computer', 'key',
         'would', 'haben', 'das', 'there', 'ich', 'du',
         'egypt', 'sunny', 'englisch', 'arabic', 'from'
]

# use randint() to create a radnom intger
index_word = random.randint(0, len(words) - 1)

# choose random word from list words
word = words[index_word]

# convert string to list 
lst_word = list(word)

# reversed list اعكس الكلام اللي في 
lst_word.reverse()

# make a string from the reversed list
#.join() أجمع الحروف بقا بستخدم 
reversed_word = ''.join(lst_word)

# fucntion time to show seconds now
start_time = time.time()

print(reversed_word)

# make a guess
guess = input('Guess the word: ')

end_time = time.time()

answer_time = end_time - start_time
print(f'{answer_time:.1f} seconds')

# check guess right or wrong
if guess == word and answer_time <5 :
    print('You won')
else:
    print('You lost')