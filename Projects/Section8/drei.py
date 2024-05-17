# answer 

# get from user , enter your money
user_money = float(input("Enter The amount of money you have: "))

print("-"*22)

# getting the price of The items
first_item = float(input("Enter The Price of The first item: "))
second_item = float(input("Enter The Price of the second item: "))
third_item = float(input("Enter The price of the third item: "))

print("-"*22)

# calculate the total price 
total_items = first_item + second_item + third_item

# if user_money >= total_items
if user_money >= total_items:
    # ture هينفذ اللي هنا وهيخرج 
    print(f"Items have been purchased successfully\nThe remaining amount is {user_money-total_items:.2f}$")
else: 
    # false نفذ اللي هنا 
    #False بعد ما الشرط اللي فوق 
    print("Sorry, You don't have enough balance")
    print(f"You need to add extra {total_items-user_money:.2f}$")

