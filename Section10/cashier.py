# Repeat the following stpes until the user enters 'exit' or press Enter 

# create a list to save inot prices
total_prices = []

while True:
    # input  the product name
    product_name = input("Enter product name: ")

    # if the user entres 'exit' or presses Enter , quit the program
    if product_name.lower() == "exit" or product_name == '':
        # break out of the loop
        break

    # input the quantity of product
    quantity = int(input("Enter Qunatity of product: "))

    # input the price
    price = int(input("The price of product: "))

    # calculate the total products cost
    total_cost = price * quantity
    total_prices.append(total_cost)

    # print the products names, quantities, prices, total cost
    print(f"Product name:{product_name}")
    print(f"Qunatity {quantity}") 
    print(f"Price: {price}")
    print("-"*15)
    
    print(f"Total Cost: {total_cost}")
    print("-"*30)
    total_cost += total_cost

# calculate the total cost of products 
receipt = sum(total_prices)

print(f"Total Receipt Cost: {receipt}")