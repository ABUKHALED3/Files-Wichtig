
message = """\n1- Add Tasks to a list 
2- Mark Tasks as complete
3- View Tasks
4- Completed Tasks
5- Quit\n"""

tasks = []
completed_tasks = []

def add_task():
    # get from user task
    my_task = input('Enter task: ').title()
    
    # define task status
    task_info = {'Task':{my_task}, 'Completed':False}

    if task_info not in tasks: 
        tasks.append(task_info)
        print('Task added to the list successfuly🥳')
    else:
        print('This task in your list Tasks\n')

def mark_task_complete():
    task = input('Enter your taks completed: ').title()
    if task in tasks:
        completed_tasks.append(task)
        tasks.remove(task)
    else:
        print(f'{task} is not in List Tasks\n')

def view_tasks():
    for index , task in enumerate(tasks):
        print(f'{index+1} {t}')
        

def view_completed_tasks():
    if completed_tasks:
        for index , task in enumerate(completed_tasks):
            print(f'{index+1} {task}\n🥳')
    else:
        print('Completed Tasks is Empty🤔')


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
        view_tasks()

    elif choice == '4':
        view_completed_tasks()
    
    elif choice == '5':
        break
    
    else:
        print('Invalid Choice, Please enter the number between 1 and 4!\n')

