# answer

# getting the number of hours and rate
hours = float(input("Enter The number of Hours: "))
rate = float(input("Enter Your Hourly Rate: "))

# The basic hour    
base_hour = 100

# the bouns 
bouns = 2
if hours > base_hour:
    over_hours = hours - base_hour
    salary = (base_hour * rate) + (over_hours * rate * bouns)
else:
    salary = hours * rate

print(f"You have worked {hours} hours this month, Your salary is {salary:,.2f}$")