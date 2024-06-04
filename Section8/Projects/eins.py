# answer 

# take from user a number to div 
# أخذ من المستخدم الرقم الذي يريد ان يقسم 
num = float(input("Enter a number: "))

# أخذ من المستخدم الرقم الذي يريد ان يقسم عليه الرقم اللي فوق
div = float(input("Enter The number to divide by: "))

print("-"*40)

print(f"The division result is {num/div:.1f}")

if num % div == 0:
    #ture
    print(f"{num} is divisible by {div}")

else:
    #false
    print(f"{num} is not divisible by {div}")