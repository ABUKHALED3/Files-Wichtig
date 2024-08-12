# A list of available fruits 
available_fruits = [ 
    # Format: [item name, price for kg] 
    ["Apple", 30], 
    ["Banana", 20], 
    ["Orange", 25], 
    ["Mango", 40], 
    ["Strawberry", 35], 
    ["Blueberry", 50], 
    ["Peach", 45], 
    ["Pineapple", 55], 
    ["Watermelon", 30], 
    ["Grapes", 50], 
    ["Cherry", 60], 
    ["Kiwi", 45] 
] 

# create a empty list of basket
basket = []

# Initialize the total_price to 0 
total_price = 0

# print this to user
print('Welcome to Shahd Fruits Store! ')

# use while loop 
while True:
    # print this to user
    print('1. View Available Fruits and buy')
    print('2. Total price of basket')
    print('3. Quit')

    # ask user abour your Choice and use int function to convert str >>> int
    input_user = input('Enter the number of your Choice: ')
    # هل الرقم اللي ادخله المستخدم 1 
    if input_user == '1':
        # True 
        print('Available Fruits: ')
        print('-'*30)
        
        # list  بلف جو الـ 
        #عشان الترقيم enumerate function استخدامت 
        for i , item in enumerate(available_fruits):
            print(f'{i+1}. {item[0]} {item[1]} EGP')
        
        print('-'*30)
        
    # ask user about choice item fruits 
        items_user = int(input('Enter the number of the item (0 to return to previous menu): '))
    
        # check if items user == 0
        if items_user == 0:
            # True 
            # أطلع فوق عيد تاني
            continue

        # Get the item the user wants to purchase 
        item = available_fruits[items_user - 1]

        # Add the item to basket
        basket.append(item)

        # Increase the total price by the item's price 
        total_price += item[1]

        # Confirm that the item has been added to the basket 
        print(f"{item[0]} added to basket successfully.") 

    # If the user chose to view the total price of the basket 
    elif items_user == '2':
        print('-'*30)
        print(f'Total price of basket: {total_price} EGP')
        
    # If the user chose to quit the program 
    elif items_user == '3': 
        # break out of the while loop
        break

    else: 
        # If the user entered an invalid choice, print an error message 
        print("Invalid choice. Please enter a number between 1 and 3.")

# If the basket is empty, print a message 
if len(basket) == 0: 
    print("Your basket is Empty.") 
 
else: 
    # Print the final basket  
    print("\nFinal basket:") 
    for item in basket: 
        print(f"{item[0]}: {item[1]} EGP.") 
 
    # Print the total price of the fruits in the basket  
    print("-"*20) 
    print(f"Total price of basket: {total_price} EGP.") 
 
# Print a goodbye message 
print("Thanks for Choosing Codezilla Fruits Store!") 
print("See you again soon!")   