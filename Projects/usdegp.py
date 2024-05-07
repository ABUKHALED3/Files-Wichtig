# get name user , remove extra spaces und capital first letter word 
name = input("Enter Your name: ").strip().title()

# Greet user
print(f"Hello,{name}")

# convert usd to egp 
# USD 1 = 47 EGP
# get from user USD to convert EGP
usd = float(input("USD: "))
egp = 47.50
exchange_rate = usd * egp

# print 
print(f"{usd}USD in {exchange_rate:,}EGP.")