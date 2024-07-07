# create a variable to save into the total of numbers
total = 0

# use while loop 
while True :

    # ask user about numbers
    num = input("Enter a number: ")

    # when user types done or enter
    if num.lower() == 'done' or num == '':
        # use break out of loop 
        break

    # convert num to float
    num = float(num)

    # if num is a positive odd or no AND
    # هل الرقم فردي  
    if num > 0 and num % 2 == 1 :
        total += num
    
    # لو الرقم مش موجب و مش بيقبل القسمة علي 3 اعمل كده 
    else:
        print(f"Error: {num} is not a positive odd numbers." )

# when while loop >>> False 
print("The Total of Positive odd numbers is",total)