# a variable to save the total 
total = 0 

# use while loop 
while True :
    
    # ask user about numbers 
    num = input('Enter a number: ')

    # when user types done or enter 
    # break out of the loop
    if num.lower() == 'done' or num == '':
        break

    # convert str to int
    num = int(num)

    # هل الرقم يقبل القسمة علي 2
    if num % 2 == 0:
        total += num

# when while loop >>> False
print(total)