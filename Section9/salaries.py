# A list of Salaries 
salaries = [
    40000 ,50000, 20000, 35475, 54784, 15756, 54745, 12578,
    15449, 54785 ,15695 ,41864, 54312, 32565, 22462, 36115,
    15245, 53225, 22133, 14052, 12404, 26476, 15646, 64120, 
    21452, 12051, 45463, 30214, 14545, 14202, 11244, 11230,
    54547, 54676, 47675, 72380, 64448, 48642, 56654, 64234,
]

# max salary use max fucntion  
max_salary = max(salaries)
print(max_salary)

# min salary use min fucntion 
min_salary = min(salaries)
print(min_salary)

print("-"*40)

# average salary sum of salaries / number of salaries

avgerage_salary = sum(salaries) / len(salaries)
print(f"Average Salary is {avgerage_salary:,.0f}")