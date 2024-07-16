#  Find the product of numbers that user enters. 

# creat a empty list of numbers 
numbers = []

# use while loop 
while True:

    # ask user about numbers 
    user_number = float(input('Enter a number: '))

    # check if user types 0 
    if user_number == 0:
        # break out of loop
        break

    # add the user number in list numbers
    numbers.append(user_number)

# Initialize a variable to save into the total cost
total_cost = 1

# list numbers عشان الف جو الـ use for loop 
for num in numbers:
    #كل مرة  num في  totalcost اضرب قيمة 
    total_cost *= num

print(f'The Product of the numbers {numbers} is {total_cost:,.2f}')