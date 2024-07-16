# a list of scores stundent 

scores = [75, 87, 93, 82, 67, 91, 88]

# create a empty list
percent_scores = []

#list عشان الف جو في  for loop هستخدم  
for score in scores:
    # % وضيف عليه  score الي str حولت 
    string = str(score) + '%'
    
    # add value string into list percent socres
    percent_scores.append(string)


print(percent_scores)