# greeting
print("It is the time to see if we could do better 😊")
print("-"*20)

# getting numbers
num = float(input("Enter the number: "))
div = float(input("Enter the number to divide by: "))

# take the yes or no 
text = input(f"{num} is divisble by {div} yes or no: ").lower()

# compare 
if num % div == 0 and text == 'yes':
    print("Bravoo 🎉🎉🎉")

else:
    print("Kein Problem , let's try again 😎")
