# a list of words 
words = [ 
        'each', 'those', 'feel', 'seem', 'high', 'place', 
'little', 'world', 'very', 'still',  
        'nation', 'hand', 'life', 'tell', 'write', 'become', 
'here', 'show', 'house', 'both',  
        'between', 'need', 'mean', 'call', 'develop', 'under', 
'last', 'right', 'move', 'thing',  
        'general', 'school', 'never', 'same', 'another', 
'begin', 'while', 'number', 'part',  
        'turn', 'real', 'leave', 'might', 'want', 'point', 
'form', 'child', 'small', 'since',  
        'against', 'late', 'home', 'interest', 'large', 
'person', 'open', 'public', 'follow',  
        'during', 'present', 'without', 'again', 'hold', 
'codezilla', 'govern', 'around',  
        'head', 'consider', 'word', 'program', 'problem', 
'however', 'lead', 'system',  
        'order', 'plan', 'keep', 'face', 'group', 'play', 
'stand', 'increase',  
        'early', 'course', 'change', 'help', 'line', 
'possible', 'fact', 'down'] 

# user input about word 
user_input = input('Enter a word: ')

# a variable to check the word is in the list or not
found = False

# use for loop search for the word
for word in words:
    if word == user_input.lower():
        print(f'word is found {user_input}')
        found = True
        #break out of the for loop
        break
    
if found != True:
    print('Wrod is not found ')

