# get a number from user between 0 >> 9 
num = float(input("Enter a number between 0 and 9: "))

# if num in ()
# هل الرقم موجود في ﻷقواس دي
if num in (1,3,7):
    # true, do this
    # لتجنب وقف البرنامج حتي نحصل علي الفكرة الذي تريد فعلها pass نستخدم الـ 
    pass
    print("You won")    
    
    # false , do this
else:
    print("You lost")

#True لازم الشرطين هنا قمتهم and
#  العكس شرط واحد فقطor

#   لو الرقم مش  أكبر من 3 و أقل من 7 
#  تعكس القيمة اللي طلع من القوس not 
if not (num > 3 and num < 7):
    # true
    print("you won again")

else:
    print("You lose again")

print("-"*20)

#num هل 8 أو 5 أقل من 
if 5 <= num <= 8:
    print("Again")

else:
    print("lose")