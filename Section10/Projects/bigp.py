"""Make a program that calculate the average of the 
second highest and second lowest numbers that are 
between 452 and 983 and are divisible by 5 and 7. 
"""
# create a empty list to save into numbers 
numbers = []

# use for loop and function range()
for i in range(452, 984):
    # هل الرقم ده يقبل القسمة علي 5 و 7
    if (i % 5 == 0) and (i % 7 == 0):
        # list لو تمام ضيف الرقم ده في 
        numbers.append(i)

# list تاني أكبر رقم في 
second_highest = numbers[-2]

#list تاني أصغر رقم في 
second_lowest = numbers[1]

# Caluclate the average 
avg = (second_highest + second_lowest) / 2

print(f'The average of the second highest ({second_highest}) ans second lowest ({second_lowest}) number is {avg} ')