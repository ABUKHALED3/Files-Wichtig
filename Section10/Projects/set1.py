# import library random 
import random 

# create a list of 1000 random numbers between 1 and 1000
lst = []

# use for loop لف لحد ما توصل الي  1000
for i in range(1000):
    # lst ضيف الرقم العشوائي اللي هيطلع في 
    lst.append(random.randint(1, 1000))

# get the unique numbers from the list
# use set function ()
# save the unique numbers in a variable
unique_nums = set(lst)

# calculate the average of the list and the unique numbers 
# average = المجوع علي العدد 
average_lst = sum(lst) / len(lst)
average_unique = sum(unique_nums) / len(unique_nums)

# print the unique numbers 
print(f'Number of unique numbers is : {len(unique_nums)}')

# print the Average of the list and the unique numbers 
print(f'The Average list numbers ist: {average_lst:.2f}')
print(f'The Average Unique numbers ist: {average_unique:.2f}')