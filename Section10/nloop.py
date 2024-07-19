# nested list
nested_list = [
    ['Hello', 'from', 'Codezilla'],
    ['Python', 'is', 'awesome'],
    ['I', 'am', 'learning', 'Python']
]

# create a vairiable to save into the letters vowels 
vowels = 'aoeiu'

# inital counter 0 
counter = 0

# loop in nested lists
for lst in nested_list:
    
    # first list in variable lst 
    # lsit خش جوه كل كلمة في 
    for word in lst:
        
        # list خش جوه كل حرف في 
        for letter in word:
            # if letter is vowel 
            if letter.lower() in vowels:
                # زود واحد
                counter += 1

print (counter)
