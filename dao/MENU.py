from dao.definitions import InsertIntoTask, UpdatePriority, UpdateNotes, UpdateBookmark, UpdateStatus, \
    InsertIntoUser, AllTasksUser, TasksBasedOnStatus, AllTasks, AssignTask
from dao.user_task_classes import ForTask, ForUser

func = input(""" Choose one:
           1.InsertIntoUser
           2.InsertIntoTask
           3.UpdatePriority
           4.UpdateNotes
           5.UpdateBookmark
           6.UpdateStatus
           7.AllTasksUser
           8.TasksBasedOnStatus
           9.AllTasks
           10. AssignTask
        """)


if func == 'InsertIntoUser':
    user_id = int(input('Enter the user_id: '))
    user_name = input('Enter the user_name: ')
    phone = input('Enter the phone number: ')
    email = input('Enter the email: ')
    role = input('Enter the role: ')
    dob = input('Enter the dob: ')
    created_on = input('Enter created_on: ')
    modified_on = input('Enter modified_on ')
    user1 = ForUser(user_id, user_name, phone, email, role, dob,
                    created_on, modified_on)
    InsertIntoUser(user1)

if func == 'InsertIntoTask':
    task_id = int(input('Enter the task_id: '))
    name = input('Enter the name: ')
    description = input('Enter the description: ')
    status = input('Enter the status: ')
    priority = int(input('Enter the priority of the task: '))
    notes = input('Enter the notes: ')
    bookmark = input('Is it bookmarked? : ')
    owner_id = int(input('Enter the owner_id: '))
    creator_id = int(input('Enter the creator_id: '))
    created_on = input('Enter created_on: ')
    modified_on = input('Enter modified_on: ')
    task1 = ForTask(task_id, name, description,
                    status, priority, notes,
                    bookmark, owner_id, creator_id, created_on,
                    modified_on)
    InsertIntoTask(task1)

if func == 'UpdatePriority':
    x = int(input("New priority: "))
    y = int(input("For task_id= "))
    UpdatePriority(y, x)

if func == 'UpdateNotes':
    x = input('Enter new notes: ')
    y = int(input("For task_id= "))
    UpdateNotes(y, x)

if func == 'UpdateBookmark':
    x = input('Bookmark?: ')
    y = int(input("For task_id= "))
    UpdateBookmark(y, x)

if func == 'UpdateStatus':
    x = input('Status?: ')
    y = int(input("For task_id= "))
    UpdateStatus(y, x)

if func == 'AllTasksUser':
    x = int(input('Enter the user_id: '))
    print(AllTasksUser(x))

if func == 'TasksBasedOnStatus':
    y = input("Choose the status, Done or Ongoing or To be started: ")
    print(TasksBasedOnStatus(y))

if func == 'AllTasks':
    AllTasks()

if func == 'AssignTask':
    x = int(input('Enter user_id: '))
    y = int(input('Enter task_id: '))
    AssignTask(x, y)




