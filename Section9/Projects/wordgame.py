# import librarys random and time
import random
import time

# list of words
words = [
'have', 'that', 'they', 'with', 'this', 'from', 'which', 'would', 'will', 
'there',
'make', 'when', 'more', 'other', 'what', 'time', 'about', 'than', 'into', 
'could', 
'state', 'only', 'year', 'some', 'take', 'come', 'these', 'know', 'like', 
'then', 
'first', 'work', 'such', 'give', 'over', 'think', 'most', 'even', 'find', 
'also', 
'after', 'many', 'must', 'look', 'before', 'great', 'back', 'through', 
'long', 
'where', 'much', 'should', 'well', 'people', 'gouda', 'just', 'because', 
'good', 
'each', 'those', 'feel', 'seem', 'high', 'place', 'little', 'world', 
'very', 'still', 
'nation', 'hand', 'life', 'tell', 'write', 'become', 'here', 'show', 
'house', 'both', 
'between', 'need', 'mean', 'call', 'develop', 'under', 'last', 'right', 
'move', 'thing', 
'general', 'school', 'never', 'same', 'another', 'begin', 'while', 
'number', 'part', 
'turn', 'real', 'leave', 'might', 'want', 'point', 'form', 'child', 
'small', 'since', 
'against', 'late', 'home', 'interest', 'large', 'person', 'open', 
'public', 'follow', 
'during', 'present', 'without', 'again', 'hold', 'codezilla', 'govern', 
'around', 
'head', 'consider', 'word', 'program', 'problem', 'however', 'lead', 
'system', 
'order', 'plan', 'keep', 'face', 'group', 'play', 'stand', 'increase', 
'early', 'course', 'change', 'help', 'line', 'possible', 'fact', 'down']

# print das from user
print('Welcome to the Reserved Words Game! ')
print('-'*25)

# random a index 
index_word = random.randint(0, len(words)-1 )

# word random of words list
word = words[index_word] 

# make a list from a string
lst_word = list(word)

# reserve the list شقلب الـ
lst_word.reverse()

# string جمع الحروف وحط كا 
reversed_word = ''.join(lst_word)

# show from user the reversed word
print(f'The reversed word is: {reversed_word}')
print('-'*25)

# strat time in seconds 
strat_time = time.time()

# guess a word 
guess = input('The word is: ')
print('-'*25)

# end time in seconds
end_time = time.time()

# calulate how take the user to ansewer
answer_time = end_time - strat_time

# check guess right or wrong
if guess == word and answer_time <= 5:
    print('You won!')
else:
    if guess != word:
        print('Wrong word!')
    if answer_time > 5:
        print('You took too long!')
    print('You lost!')