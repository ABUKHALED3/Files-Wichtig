# check if word starts with a vowel (I,O,A,U,E)

# get word from user 
word = input("Enter a Word: ")

# define vowels 
vowels = 'ioaue'

# check if  word starts with a vowel 
# if first charatar in vowels 
if word[0].lower() in vowels:
    print(f"{word} starts with a vowel")
else:
    print(f"{word} doesn't start with a vowel")
