# 90 - 100 --> A أمتياز
# 80 - 90 -->  B جيد جدا
# 70 - 80 -->  C جيد
# 60 - 70 -->  D مقبول
# 0 - 60 -->   C رأسب

# get from user the score
score = float(input("Enter a score between 0 and 100: "))

# if not 0<= socre and 100<= score
if not ( 0<= score <=100 ):
    # grade null
    grade = None
    print("Please enter a score between 0 and 100")

elif score >= 90:
    grade = 'A'

elif 80<= score:
    grade = "B"
elif 70<= score:
    grade = "C"
elif 60<= score:
    grade = "D"
else: 
    grade = 'F'

if grade is not None:
    print(f"Congratulation your score is {score} and grade is {grade}")
