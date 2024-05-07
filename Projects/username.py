# get name
# remove extra spaces around name
# replace spaces with _ 
# make all letters small
name = input("Enter your name: ").strip().replace(' ','_').lower()

# replace each "a" to "aaa"
username = name.replace("a",'aaa')
# add '@codezilla.com' to the end of the username
username = f'{username}@codezilla.com'

# print username
print(f"Your username is {username}")