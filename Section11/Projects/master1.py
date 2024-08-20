import random

# dictionary with the words and definitions 
words = { 
    # keys >>>> Vlaues
    "Absence":  "The lack or unavailability of something or someone.", 
    "Approval": "Having a positive opinion of something or someone.", 
    "Answer":   "The response or receipt to a phone call, question, or letter.", 
    "Attention":    "Noticing or recognizing something of interest.", 
    "Amount":   "A mass or a collection of something", 
    "Borrow":   "To take something with the intention of returning it after a period of time.", 
    "Baffle":   "An event or thing that is a mystery and confuses.", 
    "Ban":      "An act prohibited by social pressure or law.", 
    "Banish":   "Expel from the situation, often done officially.", 
    "Banter":   "Conversation that is teasing and playful.", 
    "Characteristic":   "referring to features that are typical to the person, place, or thing.", 
    "Cars":             "Four-wheeled vehicles used for traveling.", 
    "Care":             "extra responsibility and attention.", 
    "Chip":             "a small and thin piece of a larger item.", 
    "Cease":            "to eventually stop existing.", 
    "Dialogue":         "A conversation between two or more people.", 
    "Decisive":         "a person who can make decisions promptly.", 
    } 

while True:

    # print from user 
    print('1. Review random word')
    print('2. Test yourself')
    print('3. Exit')

    # get from the user the number
    number_user = input('Enter your choice: ')

    # make two lists 
    # word to save into the keys
    # mean to save into the vlaues

    # ues random library to use choice()
    # choice() take list , string , tuple   
    word, mean = random.choice(list(words.items()))


    # check if 
    if number_user == '1':
        print(f'word: {word}')
        print(f'Definition: {mean}')
        print('\n')
    
    elif number_user == '2':
        print(f'Definition: {mean}')

        # allow  the user to have 2 attempts to answer
        for i in range(2):
            
            answer_word = input('Enter the word: ')
            
            if answer_word.lower() == word.lower():
                print(f'Correct answer')
                
                # break out 
                break

            # if the answer is wrong 
            else:
                
                if i == 0:
                    print('Wrong answer you have 1 more attempt')
                    # كمل ينجم من فوق تاني
                    continue
                
                else:
                    print('Wrong answer you have no more attempt')
                    print(f'The correct answer is {word}')
    
    elif number_user == '3':
        break
    
    else:
        print('Invalid option')

print('Have a nice day!')
