# get the data from user
# use method .replace() to remove any spaces
data_user = input("Enter your input: ").replace(' ' ,'')

# if data_user isdigit or no?
if data_user.isdigit():
    # True 
    print(f"You Enterd a number {data_user}")

# if data_user isalpha (letters)
elif data_user.isalpha():
    # True 
    print(f"You Enterd a letters")

else: 
    print("There is a mix between letters and numbers")