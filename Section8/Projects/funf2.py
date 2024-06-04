# answer 

#print this text
print("It is the time to see height diffrentely 😉")

# get from user the height
height = float(input("Enter the height in cm: "))

if height >=200:
    tall_class ="Very Tall"

elif height >= 180:
    tall_class ="Tall"


elif 180 > height >=160:
    tall_class ="Normal"

elif height < 160 and height >= 150:
    tall_class ="Short"

else:
    tall_class ="Very short"

print(f"{height}cm is considered {tall_class}")

