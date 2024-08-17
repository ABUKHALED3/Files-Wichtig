employees = { 
    "Mohamed Hassan": {"age": 35, "salary": 20_000, 
"department": "IT"}, 
    "Ahmed Khaled": {"age": 24, "salary": 10_000, "department": 
"IT"}, 
    "Ali Hamed": {"age": 30, "salary": 15_000, "department": 
"HR"}, 
    "Mahmoud Samir": {"age": 28, "salary": 12_000, 
"department": "HR"}, 
    "Ahmed Hassan": {"age": 25, "salary": 10_000, "department": 
"IT"} 
} 


#Mohamed Hassan age
print(f'Mohamed Hassan age: {employees["Mohamed Hassan"]['age']}')
print('-'*20)

# Ali Hamed department
print(f'Ali Hamed department: {employees["Ali Hamed"]['department']}')
print('-'*20)

#  Ahmed Khaled salary 
print(f'Salary by Ahmed Khaled {employees["Ahmed Khaled"]['salary']} EGP')
print('-'*20)

mo_info = employees["Mahmoud Samir"]
message_mo = f"""Mohamed Samir is {mo_info['age']}years old, 
he works in {mo_info['department']} department and his salary {mo_info['salary']:,}"""

print(message_mo)
print('-'*20)

ahmed_info = employees["Ahmed Hassan"]
message_ahmed = f"""Ahmed Hassan is {ahmed_info['age']} years old,
he works in {ahmed_info['department']} department and his salary {ahmed_info['salary']:,}"""

print(message_ahmed)
print('-'*20)
