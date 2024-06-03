# get the data from user , Height(die Länge) Weight(das Gewicht)
height = float(input("Enter Height: ")) # use float function to convert str>>float
weight = float(input("Enter weight: "))

# convert cm to meter
meter = height / 100

# caluate BMI
BMI = weight / meter **2

# check the BMI 
# مختلفة دي جامد جدا في الحل لانها من الكبير الي الصغير
if BMI>=35:
    class_bmi = "Extreme obesity"
elif BMI>=30:
    class_bmi = "Obesity"
elif BMI>=25:
    class_bmi = "Overweight"
elif BMI>=18.5:
    class_bmi = "Normal (Healthy weight)"
else:
    class_bmi = "Underweight"

# print the result
print(f"Your BMI is {BMI:.2f} which is considerd as {class_bmi}")