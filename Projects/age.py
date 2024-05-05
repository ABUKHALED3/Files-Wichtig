# ask The user for his / her birthday year
birth_year = input("Enter Your birthday year: ")

# get current year 
current_year = input("What is current year: ")

# Subtract birh year from current year
age = int(current_year) - int(birth_year)

# print age     
print(f"Your age is {age}")