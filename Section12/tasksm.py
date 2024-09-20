# global variables
tasks = []
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
            view_tasks()

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
    
    # mark the task as completed
    task_number = int(input('Enter your taks completed: '))
    incomplete_tasks[task_number - 1]['Completed'] = True

    print('Task marked completed🥳')
    completed_tasks.append(incomplete_tasks[task_number - 1])
    

def view_tasks():
    if not tasks:
        print('No Task to view 👎') 
        return

    for i , task in enumerate(tasks,1):
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


main()