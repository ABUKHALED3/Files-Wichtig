inventory = {"Paracetamol": {"price":25, "quantity":10}, 
"Aspirin": {"price":15, "quantity":20}, 
"Ibuprofen": {"price":20, "quantity":15}, 
"Cough Syrup": {"price":30, "quantity":5}, 
"Augmentin": {"price":100, "quantity":7}, 
"Amoxicillin": {"price":80, "quantity":8}, 
"Panadol": {"price":25, "quantity":10}, 
"Zinc": {"price":15, "quantity":20}, 
"Vitamin C": {"price":20, "quantity":15}, 
"Fucidin": {"price":30, "quantity":5}, 
"Kolanog": {"price":100, "quantity":2}, 
} 

# get from the user input
user_input = input('Enter the treatment names seperated by comma (Press Enter to Exit): ').title().strip()

# make a list of reatments 
#, افصل كل حاجة لما تشوف 
treatments = user_input.split(', ')
 
# empty dict
treatments_info = {}

not_available = {'price': 'Not Available', 'quantity': 'Not Available'}

# loop through treatments    
for item in treatments:
    treatments_info[item] = inventory.get(item, not_available)

for treatment , info  in treatments_info.items():
    print(f'Item: {treatment}')
    print(f'Price {info['price']}')
    print(f'quantity {info['quantity']}')
    print('-'*20)
     