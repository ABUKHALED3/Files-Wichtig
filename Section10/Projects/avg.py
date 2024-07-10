# create a lsit to save into the scores  
scores = []

# use while loop 
while True : 
    # ask user about the grades 
    user_grades = input("Enter a score (or type 'done' to exit): ")

    # if check user types done
    if user_grades.lower() == 'done' or user_grades == '':
        # break out of the loop
        break

    # convert str >>> float and add it in the list
    scores.append(float(user_grades))


# calculate the average
avg = sum(scores) / len(scores)

print(f'The average of the scores is: {avg:0.2f}')
