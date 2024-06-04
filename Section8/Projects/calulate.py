# input data numbers und operator 
num1 = float(input("Enter the First Number: "))
num2 = float(input("Enter the Second Number: "))

# get input Operator
operator = input("Enter the Operator: ")

# check the operator 
# تمرين مهم جدا نبص عليه بردو
if operator == "+":
    result = num1 + num2
    operator_name = "Addition"
elif operator == "-":
    result = num1 - num2
    operator_name = "Subtraction"

elif operator == "*":
    result = num1 * num2
    operator_name = "Multiplication"

elif operator == "/":
    result = num1 / num2
    operator_name = "Division"

elif operator == "**":
    result = num1 ** num2
    operator_name = "Power"
else:
    print("Sorry, Please Enter Valid Input")
    operator_name = None

if operator_name is not None:
    print(f"{operator_name} result is {result}")

