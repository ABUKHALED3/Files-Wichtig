def special_sum(numbers, **kwargs): 
    
    # use get method to 
    # get the value of key
    if kwargs.get("only_even"): 
        return sum([number for number in numbers if number % 2 == 0]) 
    
    #only odd لو اليوزر كتب 
    elif kwargs.get('only_odd'):
        return sum([number for number in numbers if number % 2 != 0])
    
    elif kwargs.get('only_positive'):
        return sum([number for number in numbers if number > 0])
    
    elif kwargs.get('only_negative'):
        return sum([number for number in numbers if number < 0])
    
    elif kwargs.get('only_positive_even'):
        return sum([number for number in numbers if number % 2 == 0 and number > 0])
    
    elif kwargs.get('only_positive_odd'):
        return sum([number for number in numbers if number % 2 != 0 and number > 0])
    
    elif kwargs.get('only_negative_even'):
        return sum([number for number in numbers if number % 2 == 0 and number < 0])

    elif kwargs.get('only_negative_odd'):
        return sum([number for number in numbers if number % 2 != 0 and number < 0])
    
    else:
        return sum(numbers)
 
numbers = [1, -2, -3, 4, -5, -6, -7, 8, 9,  -10, 11, 12, 13, 14, -15, -16, 17, 18, 19, 20] 
 
print(f"Sum of all numbers: {special_sum(numbers)}\n") 
 
print(f"Total even numbers: {special_sum(numbers, only_even=True)}\n") 
print(f"Total odd numbers: {special_sum(numbers, only_odd=True)}\n") 
 
print(f"Total positive numbers: {special_sum(numbers, 
only_positive=True)}\n") 
print(f"Total negative numbers: {special_sum(numbers, 
only_negative=True)}\n") 
 
print(f"Total positive even numbers: {special_sum(numbers, 
only_positive_even=True)}\n") 
print(f"Total positive odd numbers: {special_sum(numbers, 
only_positive_odd=True)}\n") 
 
print(f"Total negative even numbers: {special_sum(numbers, 
only_negative_even=True)}\n") 
print(f"Total negative odd numbers: {special_sum(numbers, 
only_negative_odd=True)}\n") 