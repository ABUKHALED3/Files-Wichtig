# list of Salaries
salaries = [89585, 59598, 96256, 42568, 54648, 45488,98797, 15175, 66586,
            45545, 45734, 54672, 45345, 42342, 12432, 13684, 83140, 56232,
            40240, 21212, 10112, 10345, 12065, 24204, 11331, 15487, 35182,
            ]

# use method .sort() to sorted this list 
# default .sort() is sorted ascending من الصغير الي الكبير
salaries.sort()

# find the 5 largest salaries
print(f"The 5 largest salaries are in meine Firma {salaries[-5:]}")

# find the 5 smallest salaries
print(f"The 5 smallest salaries are in meien Firma {salaries[:5]}")