# find the smallest odd number 

# a list of numbers
numbers = [-500, -694, -762, -445, -348, -361, -758, -594, 
-954, -861, -610, -549, -336, -400, -600, -836, -671, -573, 
-555, -390, -450, -811, -849, -870, -815, -694, -951, -588, 
-484, -609, -674, -411, -408, -498, -649, -541, -441, -839, 
-567, -898] 

# assume the first odd number is the smallest 
for number in numbers:
    # check if the current number is odd
    if number % 2 != 0:
        smallest_odd = number
        # break out of the for loop
        break

# loop through the list of numbers    
for number in numbers:
    # check if the current number is smaller than the smallest and odd
    # و فردي  smallest_odd هل الرقم ده أقل من الرقم اللي موجود في 
    if number % 2 != 0 and number < smallest_odd:

        # update the value number
        smallest_odd = number

print(smallest_odd)