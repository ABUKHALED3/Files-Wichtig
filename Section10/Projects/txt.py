# a Average word length

sentence = """Python is a widely used high-level  
general-purpose interpreted dynamic programming language 
Its design philosophy emphasizes code readability and its 
syntax allows programmers to express concepts in fewer lines of 
code  
than possible in many other languages 
The language provides constructs intended to enable clear 
programs on both a small and large scale 
"""
# use method split to add the words in list
word_list = sentence.split()

# initial the total length 
total_length = 0

# loop through the list of words 
for word in word_list:
    # len() احفظ قيمة الـ 
    total_length += len(word)

# calculate the average word length
average_length = total_length / len(word_list)

# print the average length
print(f'The average word length is {average_length:.2f} characters')