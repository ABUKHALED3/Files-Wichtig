 # Prime number is an integer number that is only divisible by 1 and itself 

# user input 
number = int(input('Enter a number: '))

# define a Boolean Expression Flag to check if the number is prime
is_prime = True

# loop through 2 to number - 1 
for i in range(2, number):
        # check if number is divisible by any number between 2 and itself
        if number % i == 0:
                # change the Boolean Expression
                is_prime = False
                break
        
# print the result
if is_prime:
        print(f'{number} is a prime number')
else:
        print(f'{number} is not a prime number')