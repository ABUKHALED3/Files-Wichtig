def even_or(num):
    if num % 2 == 0:
        #و ملهاش دعوة بي الكود اللي تحت ده function لا القيمة ثم بتخرج من الـ return بتعمل   function الـ return لما بكتب      
        return True
    
    return False
    
# طريقة تانيه لاختصار الكود 
def is_even(num):
    # هيرجع قيمة واحد فقط 
    # False or True
    return num % 2 == 0

print(is_even(8))
    

# شرح Ternary operator
numbers = [44, 55, 75, 64, 17, 14]

even_or_odd = ['Even Number' if num % 2 == 0 else 'Odd Number' for num in numbers]

print(even_or_odd)