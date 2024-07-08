# a list to save the numbers 
numbers = []

# make a variable to use it in while loop
num = 452 

# use while loop
while num < 983:
    # if the num divisible by 5 and 7
    # هل الرقم ده يمعلم يقبل القسمه علي 7 و5 
    if num % 5 == 0 and num % 7 == 0 :
        # add the num in the list 
        numbers.append(num)
    
    # زود واحد 
    num += 1

# Get the second highest and second lowest numbers 
second_highest = numbers[-2]
second_lowest = numbers [1]   

# calculate the avgerage of the second highest and second lowest numbers
avg = second_highest + second_lowest / 2

# print the result 
print (f"The Avgerage of the second higest ({second_highest}) and second lowest ({second_lowest}) The Average is {avg}")
    
           




