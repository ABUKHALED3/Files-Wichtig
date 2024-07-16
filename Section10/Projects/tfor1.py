# a list of numbers 
numbers = [1, 2, 3, 4, 5]


# create empty list
squared_numbers = []

# numbers عشان الف جو use for loop 
for num in numbers:
    #في أوس 2 num  هنضرب قيمة الـ 
    square = num ** 2

    #list في   square ضيف قيمة الـ  
    squared_numbers.append(square)

print(squared_numbers)
