import random;

def addTask(task, taskList):
    taskList.append(task)
    return taskList

def removeTask(task, taskList):
    if task in taskList:
        taskList.remove(task)
    return taskList

def main():
    taskList = []
    print("Welcome to the task manager!")
    while True:
        print("Choose an option: \n 1. Add a task \n 2. Remove a task \n 3. View Tasks \n 4. Exit")

        user_choice = int(input("Choose an option: "))
        if user_choice == 1:
            task = input("Enter a task to add: ")
            taskList = addTask(task, taskList)
            print(f"task {task} added to the list")
        elif user_choice == 2:
            task = input("Enter a task you completed: ")
            if task not in taskList:
                print(f"task {task} not found in taskList.")
            else:
                print(f"Task {task} has been completed.")
                taskList = removeTask(task, taskList)
        elif user_choice == 3:
            if len(taskList) == 0:
                print("No tasks in the list")
            else:
                print("Tasks in the list:")
                for task in taskList:
                    print(task)
        elif user_choice == 4:
            print("Exiting task manager.")
            break
        else:
            print("Please enter a valid option.")
            user_choice = int(input("Choose an option: \n 1. Add a task \n 2. Remove a task \n 3. View Tasks \n 4. Exit"))

if __name__ == "__main__":
    main()
