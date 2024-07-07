# Always ask the user for a nummer

total = 0

while True:
    num = input('Enter a number: ')

    # if the user types done, break out of the loop
    # break ist out of loop
    # break أخرج من ام اللوب دي بقا 
    if num == 'done' or num == '':
        break
    
    #convert str to int
    num = int(num)

    # طريقة أوله    
    # if num % 2 == 0 :
    #    total += num 
    
    #continue طريقة تاني جديدة بستخدم  
    # وسيبك من السطور اللي تحت دي True أطلع فوق من الأول تاني لو 
    if  num % 2 != 0:
        continue

# False هتنفد لما فوق يبقا 
total += int(num) 

print(total)
