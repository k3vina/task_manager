import sqlite3
from task import Task

class TaskDatabase:

    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS tasks(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        description TEXT NOT NULL,
                        due_date TEXT NOT NULL, 
                        completed INTEGER)""") 

        try:
            self.cursor.execute("ALTER TABLE tasks ADD COLUMN priority TEXT DEFAULT 'Medium'")
        except sqlite3.OperationalError:
            print("Column not added!")
            pass

    def add_task(self, task):
        self.cursor.execute(
            "INSERT INTO tasks (title, description, due_date, completed, priority) VALUES (?, ?, ?, ?, ?)",
            (task.title, task.description, task.due_date, task.completed, task.priority)) 
        self.connection.commit()

    def get_all_tasks(self):
        #self.cursor.execute("SELECT * FROM tasks")
        self.cursor.execute("""SELECT * FROM tasks ORDER BY 
        CASE priority
            WHEN 'High' THEN 1 
            WHEN 'Medium' THEN 2
            WHEN 'Low' THEN 3 
        END""")
        rows = self.cursor.fetchall()
        task_list = []
        for row in rows:
            new_task = Task(row[0], row[1], row[2], row[3], row[4], row[5])
            task_list.append(new_task)
        return task_list

    def mark_complete(self, task_id):
        self.cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
        self.connection.commit()

    def delete_task(self, task_id):
        self.cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        self.connection.commit()


