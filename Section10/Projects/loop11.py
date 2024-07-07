# list of numbers
# convert this list to string 
nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29] 

# initialize the string with the first number
string = str(nums[0])

index = 1

# list  محتاج اعرف حاليا طول الـ 
# use len() function to know 
# كده عرفت الطول كام وخزنته في متغير
len_nums = len(nums)

while index < len_nums:
    # str أعمل كومه و مسافة و حط القيمة الحالية كا 
    string += ", " + str(nums[index])
    # زود واحد
    index += 1

# when while loop >>> False
print(string)


