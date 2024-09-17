# a list of grades
grades = [74, 95, 94, 67, 69]

#function النجم دي معنها اني اخلي المستخدم يحط هو الارقام جو الـ 
def average(*args):
    return sum(args) / len(args)

# اهو
result = average(71, 95, 84, 51)
print(result)