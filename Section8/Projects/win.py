# answer

# get form user name.  use lower to convert the letter lower . use capitalize to capital first letter in name
name_user = input("Enter the winning name: ").lower().capitalize()
# a list the winning names
winners = ['Mohamed','Hamza', "Ahmed" ,"Khaled"]

# if name_user in winners
if name_user in winners:
    print(f"Congratulation {name_user} is a winner!!👌")
else:
    print(f"sorry {name_user} is not a winner!🤦‍♂️")