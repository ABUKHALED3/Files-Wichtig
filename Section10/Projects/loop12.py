# a variable to save the total 
total = 0

# use while loop 
while True: 
    # get from user numbers 
    num = input("Enter a number: ")

    # stop when user types done or DONE and enter
    # if بدلا  match نبدل شوية ونستخدم  
    match num :
        case 'done' | 'DONE' | '':
            # أخرج من ام اللوب دي
            break
    # أجمع يزعيم       
    total = total + int(num) 
    
print('The Total is',total)
    