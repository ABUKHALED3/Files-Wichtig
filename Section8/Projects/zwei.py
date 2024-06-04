# ansewr 

# show from user this Text 
print("Please, Enter the Numbers you want to compare")
print("-"*25)

# get from user three numbers to compare zwischen us
num1 = float(input("Enter the First number: "))
num2 = float(input("Enter the Second number:  "))
num3 = float(input("Enter the Third number: "))
print("-"*25)

#
if num1 > num2:
    if num1 > num3:
        print(f"{num1} is the greatest number")
elif num2 > num3:
    print(f"{num2} is the greatest number")
else:
    print(f"{num3} is the greates number")

