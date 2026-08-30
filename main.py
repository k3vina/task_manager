from database import TaskDatabase
from task import Task
import sqlite3
from datetime import date

connection = sqlite3.connect("tasks.db")
db = TaskDatabase(connection)
#print("Done!")

while True:
    print("Add Task")
    print("View Task")
    print("Mark Complete")
    print("Delete")
    print("Exit")
    menu = input(f"Enter an option: ")

    if menu == "Add Task":
        id = None
        title = input("Enter the title of your task: ")
        description = input("Enter the description: ")
        due_date = input("Enetr today's date: ")
        completed = 0
        task = Task(id, title, description, due_date, completed)
        db.add_task(task)
    
