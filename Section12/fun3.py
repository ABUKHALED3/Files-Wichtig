
# بقت حاجة اختياري company is deafult = google 
# Parameters وبنكتب المدخلات اسمها function اثناء تعريف الـ 
def greet_user(name='AMR', company='google'):
    print(f'Welcome to {company} {name}')

#أقدر استخدمها صح  call to function عشان لما اعمل  
#arguments وبكتب جوها حاجة اسمها call to functionلما بعمل  
greet_user('Ahmed')

print('-'*20)

# لو عايز اغير قيمة واحد فقط 
greet_user(company='Samsung')

greet_user()

