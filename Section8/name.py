# get from user name
name = input("Enter your name: ").lower()

#موجود في الأقواس دي  value name هل  
if name in ("ahmed", "khaled" , "amr"):
    print(f"welcome {name}\nYour Id: 4547")
else:
    print("Sorry access denied")

#tuple save any data types()
#list save any data types[]

# if value name = n اخر الحرف
if name.endswith("n"):
    print("Free Palastina")