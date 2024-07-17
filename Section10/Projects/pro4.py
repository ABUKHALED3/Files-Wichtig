# Print the total of numbers that are divisible by 3 and  between 1 to 1000

# create a variable to save into the total numbers
total = 0 

# use for loop and use function range()
for i in range(1, 1001):
    # هل الرقم ده يقبل القسمة علي 3
    if i % 3 == 0:
        total += i

# print total
print(total)