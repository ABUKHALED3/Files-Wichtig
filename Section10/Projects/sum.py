#  Sum the even numbers between 28 and 928 in at least 3 different ways.

#1.
total = 0 
for i in range(28, 929, 2):
    total += i

print(total)

# 2. 
# save this numbers into numbers list
numbers = list(range(28, 929, 2))
# sum function pass list 
total = sum(numbers)
print(total)

# 3.
numbers = list(range(28, 929, 2))
total = 0
for i in numbers:
    total += i

print(total)

# 4. 
total = sum(range(28, 929, 2))
print(total)