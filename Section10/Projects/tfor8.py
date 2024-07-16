# a list of nums 
nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 
25, 27, 29] 

# create string with a first num in list and convert int>> str 
string = str(nums[0])

# use for loop 
for num in nums[1:]: 
    string+= ', ' + str(num)

print(string)