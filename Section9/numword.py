# count the number in this text

quote = """ You know, the ancient Egyptians had a beautiful belief about death. 
When their souls got to the entrance to heaven, the guards asked two questions. 
Their answers determined whether they were able to enter or not. 
Have you found joy in your life? Has your life brought joy to others?
"""

# The split method breaks down a string into a list 
# list تقطيع النص كلو الي كلمة كلمة في 
# تقطيع الكلمة بناءه علي المسافة 
list_of_words = quote.split()

print(len(list_of_words))