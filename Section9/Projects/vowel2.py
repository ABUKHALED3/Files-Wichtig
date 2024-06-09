# get a word from user 
word = input("Enter a Word: ")

# ask the user does the word starts with a vowel
answer_user = input("Does the word starts with a vowel?🤔🤔\n").lower()

# define vowels
vowels = 'aouei'

print("-"*30)

# check if first letter in word is a vowel and answer user is yes
if (word[0].lower() in vowels) and (answer_user == 'yes'):
    print("Bravooo!🥳🥳🥳")
    print(f"{word} starts with a vowel")
# check if first letter is not in vowels and answer is no
elif (word[0].lower() not in vowels) and (answer_user == "no"):
    print("Bravoo!🥳🥳🥳")
    print(f"{word} doesn't start with a vowel")

else:
    print("Let's try again😇😇")