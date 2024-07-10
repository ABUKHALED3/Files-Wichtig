# find the first multiple of 7 in a list of numbers 
numbers = [953, 776, 532, 665, 973, 683, 484, 499, 741, 980] 
i = 0 
while i < len(numbers): 
# check if the number is a multiple of 7 
    if numbers[i] % 7 == 0: 
        print(f"The first multiple of 7 is: {numbers[i]}") 
        break 
    i += 1 