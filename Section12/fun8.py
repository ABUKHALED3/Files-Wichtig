#1. def is_divisible_by(number, divisor):
#    if number % 2 == 0:
#        return True
    
#    else:
#        return False


# 2. 
#def is_divisible_by(number, divisor):
#    if number % 2 == 0:
#        return True
    
#    return False

    
#3.
#def is_divisible_by(number, divisor):
#    return True if number % divisor == 0 else False
    

#4.
def is_divisible_by(number, divisor):
    return number % divisor == 0


# get form user number und divisor
number = float(input('Enter the number: '))
divisor = float(input('Enet the divisor: '))
result = number / divisor

if is_divisible_by(number, divisor):
    print(f'{number} is divisible by {divisor} and the result is {result}')
else:
    print(f'{number} is not divisible by {divisor} and the result is {result}')
