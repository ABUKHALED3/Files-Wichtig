# get the numbers of user
x = float(input("X: "))
y = float(input("Y: "))

# ديما هي البداية if شرط الـ 
# if 1 > 6: بكتب الشرط اللي أنا عايزو مثلا  if بكتب  if عشان أقدر استخدام 
if x < y:
    #true
    print(f"X={x} is smaller than Y={y}")
# elif شرط تاني ولم تحب تضع شروط كتير نستخدم 
elif x > y:
    print("X is bigger than y")

#لايكتب جانبه شروط else 
# ديما هي النهاية 
else:
    print("x euals = y")

print("*"*30)

h = float(input("H: "))
a = float(input("A: "))
# x > y أو x < y هل الـ  
# لازم شرط منهم يتحقق عشان اقدر اطبع اللي جوه 
if h < a or h > a:
    print("h is not qual a") 
else:
    print("h eual a")