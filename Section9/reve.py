# list of operating systems
systems = ["Windows", "MacOs","Linux"]

# use method .reverse() 
# list تعكس القيمة اللي في الـ 
# in list methods لايمكن حفظها
# new_reve = systems.reverse()>>> Error
systems.reverse()
print(systems)
print("-"*40)


# convert string to list 
# use function list to make a one word to chars
name = input("Enter Your Name: ")
name = list(name)

# reverse the list
name.reverse()

# make a string from the reversed list
# join method عشان الزق الحروف ببعض
reversed_name = ''.join(name)
print(reversed_name)