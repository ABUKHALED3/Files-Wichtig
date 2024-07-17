#  Print the total of even numbers between 30 to 470. 

# create a variable to save into the total numbers 
total = 0

# use for loop and use function range()
for i in range(30, 471, 2):
    total += i

# print the total 
print(total)