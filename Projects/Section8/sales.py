# lists the code items with sales   
sales_70 = ['070','170','270','370','470']
sales_50 = ['050','150','250','350','450']
sales_30 = ['030','130','230','330','430']

# input user the data, nummer item und price
num_item = input("Enter The code of the item: ")
price_item = float(input("Enter The price of the item: "))

# check the item in lists 
if num_item in sales_70:
    discount = price_item * 0.70
    sale = "70%"
elif num_item in sales_50:
    discount = price_item * 0.50
    sale = "50%"
elif num_item in sales_30:
    discount = price_item * 0.30
    sale = "30%"
else:
    discount = price_item
    sale = "0%"

print(f"The Final Price of Item Code-{num_item} After {sale} sale is {discount:,.2f} EGP")