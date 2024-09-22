# global variables
tasks = [
    {'Task': 'Quran', 'Completed': True},
    {'Task': 'Python Kurs lernen', 'Completed': False },
    {'Task': 'ich höre und lese Deutschgeschichten', 'Completed': False},
    {'Task': 'ich will einen SpielFußball mit meiner Famile sehen', 'Completed': False},
    {'Task': 'Salah', 'Completed': True}
]
completed_tasks = []

#هحط جوها الكود الأساسي اللي تحت ده بدل ما هو سايح كده علي بعضه ويلغبط  function  هعمل 
# وزي ما حضرتك شايف الكود بقا كده منظم جدا وعشان نقدر نكتشف الاخطاء لو في خطا

def main():

    message = """\n1- Add Tasks to a list 
2- Mark Tasks as complete
3- View Tasks
4- Completed Tasks
5- Quit\n"""
    # use while loop
    while True:
        print(message)

        # get from user choice
        choice = input('Enter your Choice: ')

        if choice == '1':
            add_task()

        elif choice == '2':
            mark_task_complete()

        elif choice == '3':
            view_tasks(tasks)

        elif choice == '4':
            view_completed_tasks()
        
        elif choice == '5':
            break
        
        else:
            print('Invalid Choice, Please enter the number between 1 and 4!\n')

def add_task():
    # get from user task
    my_task = input('Enter task: ').title()
    
    # define task status
    task_info = {'Task': my_task, 'Completed':False}

    if task_info not in tasks: 
        tasks.append(task_info)
        print('Task added to the list successfuly🥳')
    else:
        print('This task in your list Tasks👎\n')

def mark_task_complete():
    # get the list of incomplete task
    incomplete_tasks = [task for task in tasks  if task['Completed'] == False ]

    if not incomplete_tasks:
        print('No tasks to mark as complete❗')
        return
    # show them to the user
    for i , task in enumerate(incomplete_tasks,1):
        print(f'{i}- {task["Task"]}')
    
    #نتيجة المستخدم  Errors بتشغل الكود ده  لو الكود ده رجع 
    # Except هيشغل اللي تحت في 
    try:
        # mark the task as completed
        task_number = int(input('Enter your taks number completed: '))
        
        if task_number < 1 or task_number > len(completed_tasks):
            print('Invalid Task number')
            return
        
        incomplete_tasks[task_number - 1]['Completed'] = True

        print('Task marked completed🥳')
        completed_tasks.append(incomplete_tasks[task_number - 1])
    
    # لو المستخدم شغل البرنامج غلط 
    #وينفذ اللي فيها  except هيخش جو الـ 
    # ده في حالة أني المستخدم ادخل قيمة غلط او استخدام البرنامج غلط
    # وكده احنا بنبعد عن اخطاء في البرنامج 
    
    # valueError لو المستخدم عمل 
    # خش نفذ اللي جو هنا
    except ValueError:
        print('Invalid Input, Please Enter a number')
    


def view_tasks(tasks_list):

    if not tasks_list:
        print('No Task to view 👎') 
        return

    for i , task in enumerate(tasks_list,1):
        status = '✔️' if task['Completed'] else '❌'

        print(f'\n{i}- {task['Task']} {status}')
        

def view_completed_tasks():
    if completed_tasks:
        for i , task in enumerate(completed_tasks,1 ):
            for value in task.values():
                if value is not True:
                    print(f'{i} {value} 🥳')
    else:
        print('Completed Tasks is Empty🤔')


#__main__ لما استخدم المتغير ده جو الملف ده واشغل الملف ده بيرجع 
#لي الملف ده في ملف اخر  import لكن لما بعمل 
#لي اسم الملف ده  retrun  بيعمل 
# المثال ده في الملف
# new_tasks
print(__name__)

if __name__ == '__main__':
    main()