# print this text to user
print("It is the time to see if we could do better 😎")

print("-"*20)

num = float(input("Enter the number: "))

text = input(f"{num} is even or odd?🤔 ")

if (num%2==0 and text == "even") or (num %2!= 0 and text == "odd"):
    print("Bravoo🎉🎉🎉")
else:
    print("No problem, Let's try again ❤")
    