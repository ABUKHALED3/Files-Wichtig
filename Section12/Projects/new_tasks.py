from datetime import datetime 
import tasksm


tasks = []

def add_task():

    tasksm.add_task()

    # get from user task date
    task_user_date = input('Enter Task date (yyy-mm-dd): ')

    # use library datetime to check 
    # هل التاريخ اللي هيكتبو المستخدم تمام ولا لا
    try:
        datetime.strptime(task_user_date, '%Y-%m-%d')
        task_info = {'Task': ts}
        tasks.append(task_info)
        
    except ValueError:
        print('Invalid date format. Please enter a date in yyy-mm-dd format\n')


def mark_task():
    pass

def view_tasks():
    pass



def main():
    message = """1. Add task to list 
2. Mark task as complete
3. View Tasks
4. Quit
"""

    # use While loop to print immer this message
    while True:
        print(message)

        # get from user choice
        choice = input('Enter your choice: ')

        # check user write was?
        # بشوف المستخدم هيكتب اي
        if choice == '1':
            add_task()
            print(tasks)

        
        elif choice == '2':
            mark_task()
        
        elif choice == '3':
            view_tasks()
        
        elif choice == '4':
            break

        else:
            print('Invalid input! Enter a number between 1 to 4\n')

main()
