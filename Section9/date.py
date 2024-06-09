# use the split mehtod to break down birth date into day, month, year

# get the birth date from user
birth_date = input("Enter your birth date (dd-mm-yyyy): ")

# using the split method to breaks down string into a list and save into variables
day , month , year = birth_date.split("-")
# print
print(day , month , year)