# print this text 
print("Please Enter scores between 0 and 100 ")
print("-"*20)

# input data 
sub1 = float(input("Enter Arabic Score: "))
sub2 = float(input("Enter English Score: "))
sub3 = float(input("Enter Math Score: "))
sub4 = float(input("Enter Physics Score: "))
sub5 = float(input("Enter Biology Score: "))
sub6 = float(input("Enter Chemistry Score: "))

print("-"*20 )

# calulate the Average 
score = (sub1 + sub2 + sub3 + sub4 + sub5 + sub6) / 6

# مهم جدا التمرين ده لازم نبص عليه 
if not (0<=score<=100):
    class_grade = None
    print("Please, Enter a score between 0 and 100")

elif score >= 90:
    class_grade = 'A'
elif score >= 80:
    class_grade = 'B'
elif score >= 70:
    class_grade = 'C'
elif score >= 60:
    class_grade = 'D' 
else:
    grade = 'F'

if class_grade is not None:
    print(f"Your Socre is {score:.2f}%\nYour grade is {class_grade}")