# import library random 
import random 

# save the random number in the variable 
random_num = random.randint(1,100)

user_guess = 0
num_try = 0

# use while loop 
while user_guess != random_num:
    
    # ask user about your guess
    user_guess = int(input("Guess the number: "))
    
    if user_guess > random_num:
        print("Too high , try again")
    
    elif user_guess < random_num:
        print("Too low, try again")

    # addtion 1 
    num_try += 1

# End of the program 
print(f"You guessed the number in {num_try} attempts")