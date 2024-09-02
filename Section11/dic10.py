# a letter 
txt = """Welcome to codezilla course we are happy to have you
all here hope you enjoy the course"""

# use method count 
# بتعد الحاجة اللي انت اديتها ليها 
print(txt.count('a'))

# define a dict to store the letters
counter_letter = {}

# use a for loop to loop through the string
for letter in txt :
    if letter in counter_letter: 
    # check if letter is in dict Ture >>> add 1 to the value 
        counter_letter[letter] +=1
    
    # False >>> add the letter to dict, set it's value to 1  
    else : 
        counter_letter[letter] = 1

print(counter_letter)