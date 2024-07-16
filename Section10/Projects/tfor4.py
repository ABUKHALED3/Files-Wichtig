# list of names 
names = ["mohamed gouda", "islam mahfouz", "ayman hamed", "hassan ali", 
"mostafa mohamed", "hesham khaled" , "amr khaled"] 

# Initialize empty list
title_names = []

# use for loop 
for name in names:
    # add each name in list title names and use method .title()
    title_names.append(name.title())

# when for False print the list
print(title_names)