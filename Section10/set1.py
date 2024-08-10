# lektion fur sets 

# a list of numbers 
numbers = [2,3,1,2,3,4,4,5,6,4,5,6,1,2,3,4,7,1,2,3,7,5,6,7]

# use set function 
# set function take one argumet any iterable >> list - string - tuple 
# و تقوم بترتيب من الصغير الي الكبير و لا يوجد اي قيمة متكرار جوها
unique_numbers = set(numbers)
print(unique_numbers)
print('-'*40)

# str
name = 'AhmedAhmed'
name_edit = set(name)
print(name_edit)
print('-'*40)


# create a new empty list
unique_list = []

# use for loop through a list of numbers
for number in numbers:
    # check if number not in unique list
    if number not in unique_list:
        # True append number
        unique_list.append(number)

print(unique_list)

