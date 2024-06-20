# list of names
names = ['Ahmed', 'Hesham', 'Eslam', 'Mohamed']

# use method .copy() to copy this list and play in this list copy
names_copy = names.copy()

# use method addend to add a value in end this list
names_copy.append(4.5)
print(names_copy)
print(names)

print("-"*40)


# another soultion to copy a list
names_copy2 = names[:]

# use extend method .extend() to add a value in this list
new_names = ["Amr", "Hamza", "Wgez", "Marwan"]
names_copy2.extend(new_names)

print(new_names)
print(names)