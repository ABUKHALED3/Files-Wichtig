# ein Bericht
txt = """One of the most effective ways to reduce the friction 
associated with 
your habits is to practice environment design 
In a previous chapter we discussed environment design as a 
method for making cues more 
obvious but you can also optimize your environment to make 
actions 
easier 
For example when deciding where to practice a new habit it is 
best to choose a place that is already along the path of your 
daily 
routine 
Habits are easier to build when they fit into the flow of your 
life  
You are more likely to go to the gym if it is on your way to 
work 
because stopping does not add much friction to your lifestyle 
""" 

# make the string lower case and remove the new line and spaces 
txt = txt.lower().replace('\n', '').replace(' ','')

# cerate empty dict 
letter_counter = {}

# use for loop through txt
for letter in txt:
    if letter not in letter_counter:
        # add to key value 1
        letter_counter[letter] = 1
    else: 
    # if the letter is in the dictionary add 1 to the value 
        letter_counter[letter] += 1 


# print the dict
for letter , count in letter_counter.items():
    print(f'{letter.title()}: {count}')