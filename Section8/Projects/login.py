# first user data
first_username = "ahmed_khaLed@afi.com"
first_password = "ilovepython400!"

# second user data
second_username = "der_arzt@yahoo.com"
second_password = "ichbinahmed#1"

# input data from user
check_username = input("Enter username: ")
check_password = input("Enter password: ")

# check the data ist richtig
if (check_username == first_username and check_password == first_password) or \
    (check_username == second_username and check_password == second_password):
    print("Access is allowed")
else:
    print("sorry, access is nicht allowed ")