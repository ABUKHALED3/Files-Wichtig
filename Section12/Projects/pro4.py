numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9] 

def sum_odd_numbers(numbers): 
    total_odd = 0
    for number in numbers:
        if number % 2 != 0:
            total_odd += number
        
    return total_odd
        
print(sum_odd_numbers(numbers))