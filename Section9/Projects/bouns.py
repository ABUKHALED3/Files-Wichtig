# employess and their ids
seniors =  ['1470','40050','9009','6784']
mid_level =  ['2001', '3004','1315' ,'1325']
juniors = ['30040','30010','30060','80014']

# juniors * 3  (mid_level * 6) (seniors * 9 )

# get the data from user
id_employee = input("Enter Employee id: ")
rate = float(input("Enter Hourly Rate: ")) # use float function to (covert >> str >>> float)
hours = float(input("Enter Hours Worked this month: "))

# check id employee in seniors
if id_employee in seniors:
    # Ture calulate das
    salary =  rate * hours * 9

# check id employee in mid level
elif id_employee in mid_level:
    # True calulate das
    salary = rate * hours * 6

# check id employee in juniors
elif id_employee in juniors:
    # True claulate das
    salary = rate * hours * 3

# if id not in thier employees
else:
    print("Not a employee")
    salary = None

# print das when salary Not equal None
if salary is not None:
    print(f"Employee id: {id_employee} gets a bouns of {salary:,.2f} EGP")