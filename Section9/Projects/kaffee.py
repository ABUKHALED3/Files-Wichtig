# A list oder menu in cafe
menu =[ 
        # list Hot Drinks
        ['Tea $1','Herbs $2','Hot Cider $3','Coffee $4','Hot Chocolate $4'],
        #list Soda
        ['Cola $1','Pepsi $2', 'Fanta $2','Sprite $1','Mirinda $2'],  
        # list Juices
        ['Lemonade $1','Orange Juice $1','Mangi Juice $2','Apple Juice $2','Strawberry']
]
types_drinks = """1.Hot Drink
2.Soda
3.Juices      
 """
# print types drinks und chosse type drink 
order_index_drink = int(input(f"{types_drinks}\nEnter the type of the drink you want to order: "))


# A message to ask the user for the drink 
message_drink = f""" 
Please, Enter the number of the drink you want to order:
1.{menu[order_index_drink - 1][0]}
2.{menu[order_index_drink - 1][1]}
3.{menu[order_index_drink - 1][2]}
4.{menu[order_index_drink - 1][3]}
5.{menu[order_index_drink - 1][4]}

"""

# get the drink 
order_index = int(input(message_drink))
print("-"*30)

order = menu[order_index_drink - 1][order_index-1]

# print the order
print("Thanks for choosing ABUKHALED Cafe! 🫖 👍")
print(f"Please, Enjoy your Time\nWhile we get {order} ready for you.")