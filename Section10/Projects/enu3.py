books = [ 
    ("The 7 Habits of Highly Effective People", "Stephen R. Covey"), 
    ("How to Win Friends and Influence People", "Dale Carnegie"), 
    ("Atomic Habits", "James Clear"), 
    ("The 4-Hour Work Week", "Tim Ferriss"), 
    ("Deep Work", "Cal Newport"), 
    ("So Good They Can't Ignore You", "Cal Newport"), 
    ("Digital Minimalism", "Cal Newport"),]

# 2. Book: How to Win Friends and Influence People - Author: Dale Carnegie 

# use for loop through in list of books
# use enumerate function() عشان الترقيم
for i , book in enumerate(books , 1):
    print(f'{i}. Book: {book[0]} - Author: {book[1]}')