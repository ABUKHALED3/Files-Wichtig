numbers = [1, 24, 57, 67, 78, 1, 0, 47, 7]

def max_even(numbers):
    even_numbers = [num for num in numbers  if num % 2 == 0]
    if even_numbers:
        return max(even_numbers)
    else:
        return None
    
print(max_even(numbers))

    






            