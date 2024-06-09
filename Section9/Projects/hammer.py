text_1 = "Jetzt ist die beste Zeit, Das is der Hammer!🔨"

# count with the spaces
print(len(text_1))

#remove spaces
remove_spaces = text_1.replace(" ","")

print(len(remove_spaces))

print("-"*40)

# another task
text_2 = """A computer is a digital electronic machine 
that can be programmed to carry out sequences of 
arithmetic or logical operations automatically""" 

remove_spaces2 = text_2.replace(" ", "")
# print the number of characters with spaces
print(f"Number of characters with spaces: {len(text_2)}")

# print the number of characters without spaces:
# use method replace to remove spaces
print(f"Number of characters without spaces: {len(remove_spaces2)}")