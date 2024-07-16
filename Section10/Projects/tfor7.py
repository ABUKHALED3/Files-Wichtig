# A list of prices 
prices = [75, 153, 635, 144, 356, 712, 675, 234]

# create a veriable to save into how many numbers in list
count = 0 

# create a veriable to save into the sum numbers  
total = 0 

# list تاني عشان الف جو for loop
for price in prices:
    #priceعلي اللي في  sum اجمع اللي في  
    total += price
    # زود واحد هنا عشان اقدر اعرف عدد الارقام
    count += 1 

# calculate the average price 
avg = total / count  

# print the average price
print(f"The average is {avg:.2f}")

