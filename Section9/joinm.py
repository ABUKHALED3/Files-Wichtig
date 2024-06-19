# list of fruits
fruits = ['apple', 'orange', 'watermelon', 'grapes' , 'mango' , 'pineapple', 'kiwi', 'Banana']

# get order
fruit = input("Which fruit do you want: ")

# use join method to return a one string
fruits_join = ', '.join(fruits[:-1])
fruits_str = f'{fruits_join} and {fruits[-1]}'

# check if the fruit is available 
# use method lower to convert input user 
if fruit.lower() in fruits:
   
    # ask user for amount
    amount = input("Enter amount in kg: ")
    print(f"We will get you {amount} kg {fruit} very soon")

else:
    print(f"Sorry, We only have {fruits_str}")

