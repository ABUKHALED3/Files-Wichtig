nums = [44, 64, -12, 0, -5, 34, -55, 67, -88, -99] 

# abs remove - 
nums_positive = [abs(num) for num in nums if num < 1]
print(nums_positive)