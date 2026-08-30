from database import TaskDatabase
from task import Task
import sqlite3
from datetime import date
import os

# connects the CLI interface to the database
connection = sqlite3.connect("tasks.db")
db = TaskDatabase(connection)
#print("Done!")

while True:
    #if os.name == "nt":
    #    os.system("cls")
    #else:
    #    os.system("clear")


    print("Add task")
    print("View task")
    print("Mark complete")
    print("Delete")
    print("Exit")
    menu = input(f"Enter an option: ")
    #print(repr(menu))

    # adds tasks to the database
    if menu == "Add task":
        id = None
        title = input("Enter the title of your task: ")
        description = input("Enter the description: ")
        due_date = input("Enter the due date: ")
        completed = 0
        task = Task(id, title, description, due_date, completed)
        db.add_task(task)

    # lets the user view the tasks written
    if menu == "View task":
        task_list = db.get_all_tasks()
        if len(task_list) == 0:
            print("No tasks found.")
        else:
            print(task_list[0].header_row())
            for task in task_list:
                print(task.to_row())
        

    # marks tasks complete once done
    if menu == "Mark complete":
        task_id = int(input("Which the id of the task you want to mark as complete? "))
        db.mark_complete(task_id)

    # deletes a task
    if menu == "Delete":
        task_id = int(input("Which task do you want to delete? "))
        db.delete_task(task_id)

    # exits the menu system
    if menu == "Exit":
        db.connection.commit()
        db.connection.close()
        print("Goodbye! See you later.")
        break


