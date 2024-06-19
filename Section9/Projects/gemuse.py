# list of available vegetables 
vegetables = ['broccoli', 'eggplant', 'carrot', 'cabbage',  
'cucumber', 'potato', 'garlic', 'pepper']

# تحية كده للمعلم
print("Willkommen at AKA Gemüse!")

# get order from user
vegetable = input("Enter the vegetable you want to get: ")
print("-"*40)

# use method join to control 
vegetable_join = ", ".join(vegetables[:-1])
vegetables_str = f"{vegetable_join} and {vegetables[-1]}"

# check if the vegetable is available 
if vegetable in vegetables:
    # ask for amount
    amount = input("Enter the amount in kg: ")
    print(f"We will get you {amount} kg of {vegetable} very soon")
else:
    print(f"Sorry, we only have {vegetables_str}")