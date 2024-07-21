words = [["Hello", "from", "Codezilla"],  
["Python", "Course", "is", "awesome"],  
["I", "enjoy", "learning", "Python", "with", "Codezilla"]] 

# make a list of sentences 
sentences = []

# loop through the list
for lst in words:
    # convert each inner list to a string and join them with a space 
    sentences.append(' '.join(lst))

# make another list named modified_sentences 
modified_sentences = []

# Loop through the list of sentences 
for i in range(len(sentences)):
    # Replace Spaces with dashes and convert to uppercase 
    modified_sentences.append(sentences[i].replace(' ',' -').upper())


# Print the sentences and modified_sentences 
print(f"The list of sentences is: {sentences}") 
print(f"The modified list of sentences is: {modified_sentences}")