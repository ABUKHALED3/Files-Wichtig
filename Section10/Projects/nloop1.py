# 1. 
nested_list = [["Hello", "from", "Codezilla"],  
["Python", "Course", "is", "awesome"],  
["I", "enjoy", "learning", "Python", "with", "Codezilla"]]

# create a empty list 
flat_list = []

# using .extend() method 
for lst in nested_list:
    #حطها في الجديدة دي  list كل  
    flat_list.extend(lst)

# print lsit
print(flat_list)


# solution 2 using .append() method

nested_list = [["Hello", "from", "Codezilla"],  
["Python", "Course", "is", "awesome"],  
["I", "enjoy", "learning", "Python", "with", "Codezilla"]]

flat_list = []

# use nested loop 
for lst in nested_list:
    
    # list خش في كل كلمة من 
    for word in lst:
        # ضيف كل كلمة 
        flat_list.append(word)

print(flat_list)