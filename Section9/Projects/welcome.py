# get name of user 
# use method strip to remove spaces 
# use method title to capital a first letter
name = input("Enter your name: ").strip().title()

# search idx spaces 
space_idx = name.index(" ")
 
first_name = name[:space_idx]

print(f"Hello, {first_name}\nWelcome at Codezilla!😊")
