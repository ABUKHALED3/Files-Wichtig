txt = """welcome to codezilla course 
we are happy to have you all here 
hope you enjoy the course""" 

# use method setdefault to count the letter 

# a define a empty dict
counter_letter = {}

# use for loop through txt 
for letter in txt: 
    # add the letter in dict and value  0
    counter_letter.setdefault(letter, 0)

    # add 1 the value of the letter
    counter_letter[letter] += 1

print(counter_letter)