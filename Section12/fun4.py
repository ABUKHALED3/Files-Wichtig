# functions اي حاجة بره الـ 
#Global Scope اقدر استخدمها في كل حته وهي اسمها 

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

#functions  اي حاجة جو الـ 
#Lock Scope  بس واسمها functions بستخدمها جو الـ 

def sum_even(even_numbers):
    total = 0
    for number in even_numbers:
        if number % 2 == 0: 
            total += number
    
    #عشان اقدر استخدم المتغير في البرنامج  return total 
    return total
                 
# result = 42
result = sum_even(numbers)
print(result)

print(sum_even([1,4,2,4]))
print(sum_even((1,45,7,6,7,8)))