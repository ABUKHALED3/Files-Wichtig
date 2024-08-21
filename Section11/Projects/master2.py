# available treatments 
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

# use while loop
while True:
    # get input from the user
    user_input = input('Enter treatment name (Press Enter to Exit): ').title()


    if user_input == '':
        break
    

    item = inventory.get(user_input, 'Not Available')

    if item != 'Not Available':
        print(f'{user_input}: ')
        print(f'price: {item['price']}')
        print(f'{item['quantity']}')
    
    else:
        print(item)