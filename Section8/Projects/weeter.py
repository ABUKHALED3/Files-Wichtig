print("let's see how we could deal with the weather 😊")
print("-"*20)

degree = float(input("Enter the degree in Celsius: "))
print("-"*20)

# Weather info
extremely_hot ="""When the degree is 40 or more
We could say that the weather is extremely hot 🔥🔥
We should also remember to drink a lot of water 💦
We should aviod direct exposure to The Sun ☀️
""" 
very_hot = """When the degree is 30 or more 
We could say that the weather is very hot♨️♨️
We should also remember to drink a lot of Water💦
We should be careful about exposure to The Sun ☀️ 
"""

moderate = """When the degree is between 20 und 30 
We could say that we have the moderate or good weather👍
We should not go with too heavy clothes or light clothes 👕 
 """

cold = """When the degree is between 10 und 20  
We could say that we have cold weather ❄️
We should not go with pretty heavy clothes 👚
 """

very_cold = """When the degree is between 0 und 10 
We could say that we have very cold weather 🥶🥶
We should go with pretty heavy clothes👚
 """

extremely_cold = """When the degree is less than 0 
We could say that we have extremely cold weather ❄️❄️🥶🥶
We should go with really heavy clothes 👕👚
We should aviod getting out as possible🙆‍♂️🙆‍♂️
Never forget your Heavey Jacket When you are going out 🧥🧥 
"""

# مهمه جدا ده نبص عليه كتير جدا ومراجعة
if degree>=40:
    print(extremely_hot)
elif degree>=30:
    print(very_hot)
elif degree>=20:
    print(moderate)
elif degree>=10:
    print(cold)
elif degree>=0:
    print(very_cold)
else:
    print(extremely_cold)
