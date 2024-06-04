# index from 0  من هذا بعدد ال value عشان أختار أي  
# العدد بيتم من  0 من الشمال الي اليمن  
# index -1 من اليمين الي الشمال 
names = ['Ahmed', 'Omar', 'Amr', 'Eslam','Khaled']

# list and [int number index hier] أكتب أسم  
print(names[2])
# right to left start with 1- 
print(names[-2])

print('-'*20)

# nested list 
nums = [
    #index[0][]
    [1,2,3,4,5],
    #index[1][]
    [2,4,6,8,10,0]
]

#second []رقم القيمة نفسها اللي عايز اطبعها, first [] اللي عايز اطبع منها اي قيمة list رقم ال 
print(nums[1][5])