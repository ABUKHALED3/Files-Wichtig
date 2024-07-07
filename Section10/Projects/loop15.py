# create a variable to save total of numbers 
# هنا 1 عشان الضرب
total = 1 

# use while loop
while True :
    # ask user about numbers 
    num = input("Enter a number: ")

    # when user types done or enter
    if num.lower == "done" or num == '':
        # break out of the loop
        break 
    
    # convert str to float
    num = float(num)

    # هل الرقم مش بيساوي صفر
    if num != 0 :
        total *= num

# when while loop >>> False 
print(total)