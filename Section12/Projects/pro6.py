

def count_positive_even_numbers(*args):
    positive_even = [number for number in args  if number % 2 == 0 if number > 0]
    if positive_even:
        return sum(positive_even)
    else:
        return None



count_positive_even = count_positive_even_numbers(1, 2, 3,-4, -6, -7, 8, 9, 11)

print(count_positive_even)