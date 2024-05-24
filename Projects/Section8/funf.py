# answer

# print this text to user
print("It is the time to see height differently 😊 ")

# get from user the number 
num = float(input("Enter the height in cm: "))

print("-"*20)

# check if num > 200
if num >= 200:
    # ture
    print(f"{num} cm is considered Very tall")

# بين الـ 180 الي 200
# طريقة أوله
elif not(num <= 180 and num < 200):
    print(f"{num} cm is considered Tall")

# بين الـ 160 الي 180
# طريقة أخري
elif 160 <= num < 180:
    print(f"{num} cm is considered Normal")

# بين الـ 150 الي 160
elif 150 <= num < 160:
    print(f"{num} cm is considered short")

else:
    print(f"{num} cm is considered very short")


