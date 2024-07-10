# use while loop 
while True:

    # ask user
    user = input('> ') 

    # ignoring blank lines and #
    if user.startswith('#') or user == '':
        # وعيد تاني loop أطلع فوق عند
        continue
    
    #  check if user types done 
    if user.lower() == 'done':
        # break out of the loop
        break

    print(user) 

# End of The program
print('Done!')