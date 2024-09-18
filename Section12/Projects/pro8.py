
def is_divisible_by(number, divisor, even=False):
    if even:
        return 'Gerade Zahl' if number % 2 == 0 else 'Ungerade Zahl'
    
    return number % divisor == 0




print(is_divisible_by(44, 2))
    