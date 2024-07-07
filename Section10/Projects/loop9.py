# variable count in the first 1
count = 1

# total by 0 
total = 0

while count <= 1000:

    # if the numbers divisible by  3
    # هل الرقم يقبل القسمة علي 3
    if count % 3 == 0:
        
        # sum total with count
        total += count
    
    # زود واحد يزعيم
    count +=1

print('The Total is',total)