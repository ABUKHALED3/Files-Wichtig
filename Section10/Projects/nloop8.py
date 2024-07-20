lst_words = [['have', 'that', 'they', 'with', 'this', 'from', 
'which', 'would', 'will', 'there', 'make', 'when', 'more', 
'other', 'what', 'time', 'about', 'than', 'into', 'could'],

[ 'state', 'only', 'year', 'some', 'take', 'come', 'these', 
'know', 'like', 'then', 'first', 'work', 'such', 'give', 
'over', 'think', 'most', 'even', 'find', 'also', 'after', 
'many', 'must', 'look', 'before', 'great', 'back', 'through', 
'long'],

[ 'where', 'much', 'should', 'well', 'people', 'gouda', 'just', 
'because', 'good', 'each', 'those', 'feel', 'seem', 'high', 
'place', 'little', 'world', 'very', 'still', 'nation', 'hand', 
'life', 'tell', 'write', 'become', 'here', 'show', 'house', 
'both', 'between', 'need', 'mean', 'call', 'develop', 'under', 
'last', 'right', 'move', 'thing'],  

['general', 'school', 'never', 'same', 'another', 'begin', 
'while', 'number', 'part', 'turn', 'real', 'leave', 'might', 
'want', 'point', 'form', 'child', 'small', 'since', 'against', 
'late', 'home', 'interest', 'large', 'person', 'open', 
'public', 'follow', 'during', 'present', 'without', 'again', 
'hold', 'codezilla', 'govern', 'around', 'head', 'consider', 
'word', 'program', 'problem', 'however', 'lead', 'system'],

['order', 'plan', 'keep', 'face', 'group', 'play', 'stand', 
'increase', 'early', 'course', 'change', 'help', 'line', 
'possible', 'fact', 'down']] 

# define a counter for 'a' and 'e'
counter_a = 0 
counter_e = 0

# for loop through the list of words
# list هنا بلف في الـ 
for lst in lst_words:
    
    # loop through the words in list
    # list هنا بلف جو الكلمة اللي في 
    for word in lst:

        # هنا بلف جو الحروف اللي في الكلمة 
        for letter in word:
            
            # a هل الحرف ده 
            if letter == 'a':
                # زود واحد
                counter_a += 1
            
            # e هل الحرف ده 
            elif letter == 'e':
                #زود واحد 
                counter_e += 1

# print the result 
print(f"The number of letter 'a' in words is {counter_a}")
print(f"The number of letter 'e' in words is {counter_e}")
