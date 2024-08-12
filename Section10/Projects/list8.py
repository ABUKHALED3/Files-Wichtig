import random 
# make list with 20 random numbers between 100 and 1000 using 
# list comprehension and random.randint() 

random_nums = [random.randint(100, 1_000) for _ in range(20)] 
print(random_nums) 