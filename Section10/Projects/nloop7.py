# list of numbers
numbers = [-500, -694, -762, -445, -348, -361, -758, -594,  -954, -861, -610, 
-549, -336, -400, -600, -836, -671, -573,  -555, -390, -450, -811, -849, -870, 
-815, -694, -951, -588,  -484, -609, -674, -411, -408, -498, -649, -541, -441, 
-839,  -567, -898]

# create a epmty list to store positive numbers
positive_numbers = []

# loop through the list
for number in numbers:
    
    # هضرب الرقم في -1 عشان أطير السالب 
    number *= -1
    
    # add the number to the list
    positive_numbers.append(number)

print(positive_numbers)


# solution 2 

# a list of numbers 
numbers = [-500, -694, -762, -445, -348, -361, -758, -594,  -954, -861, -610, 
-549, -336, -400, -600, -836, -671, -573,  -555, -390, -450, -811, -849, -870, 
-815, -694, -951, -588,  -484, -609, -674, -411, -408, -498, -649, -541, -441, 
-839,  -567, -898]

# empty list to store positive number
positive_numbers = []

# loop through the list
for number in numbers:
    # use a abs() function to delete negative und add the number in list
    positive_numbers.append(abs(number))

print(positive_numbers)