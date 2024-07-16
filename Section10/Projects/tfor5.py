# Make a list from the letters of the user string in uppercase.

# eInitalizl empty list 
letters = []

# ask user about text
text_user = input("Enter your Text: ")

#عشان اقدر الف جو النص الذي ادخله use for loop 
for char in text_user:
    # add char value as capital letter into the list
    letters.append(char.upper())

# print the list
print(letters)