# تعريف function

def greet_user(name):
    message_greet = f"""Welcome {name.title()} at Codezilla Course
Enjoy your Learning Journey"""
    print(message_greet)

# get from user name
name_uesr = input('Please enter your name: ')

# call greet_user function
greet_user(name_uesr)
