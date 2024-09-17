nums = [1, 2, 7, 6, 4, 5, 3, 8, 9, 10 ,-11 , -4, -7, -1]

def special_sum(numbers, only_even=False, only_odd=False, only_pos=False, only_neg=False):
    total = 0

    for num in numbers:

        if only_even:    
            if num % 2 == 0 and num > 0:
                total += num
    
        elif only_odd:
             if num % 2 != 0 and num > 0:
                total += num
        
        elif only_pos:
            if num > 0:
                total += num
        
        elif only_neg:
            if num < 0:
                total += num
        
        else:
            total += num
    
    return total


print(special_sum(nums))