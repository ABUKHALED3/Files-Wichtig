# get from user the data 
num = input("Enter The Opreation: ")

# get first num and second num
# useing method split to break down str into list 
# save value in variables and convert str >>> int  
first_num = int(num.split()[0])
second_num = int(num.split()[2])

# get the opreation 
opr = num.split()[1]

total = None
# check the opreation
if opr == "*":
    total = first_num * second_num
    name_opreation = "Multiplication"
elif opr == "/":
    total = first_num / second_num
    name_opreation = "Division"
elif opr == "+":
    total = first_num + second_num
    name_opreation = "Additional"
elif opr == "-":
    total = first_num - second_num
    name_opreation = "Subtraction"
elif opr == "**":
    total = first_num ** second_num
    name_opreation = "Power"
else:
    print("Please, Write a correct opreation")

if total is not None:
    print(f"{name_opreation} result is {total}")
