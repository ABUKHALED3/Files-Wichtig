# lektion fur definition functions 
# function ازي أعرف 

# def بكتب 
# function ثانيا اسم الـ 
# افتح أقواس و نقطتين

#جو القوس argument بكتب  function takes argument عشان اخلي الـ 
def greet_user(name, age):
    print(f"Welcome to Codezilla {name} your age is {age}")

# get from user name und age
name = input('Enter your name: ')
age = input('Enter your age: ')

# call to function
greet_user(name, age)