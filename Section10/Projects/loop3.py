# print numbers -99 >>>  99

# first negative odd number
odd_num = -99

# use while loop 
while odd_num < 100:
    
    # print the current value of odd num if it's negative and odd
    if odd_num < 0 and odd_num % 2 != 0:
        print(odd_num)

    odd_num += 2