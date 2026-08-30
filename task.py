from datetime import date

class Task:
    
    def __init__(self, id, title, description, due_date, completed):
        self.id = id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = completed

    
    def display_info(self):
        print(f"id: {self.id}")
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Date: {self.due_date}")
        print(f"Completed: {self.completed}")


if __name__ == "__main__":
    my_task = Task("1", "To-Do List", "Today's activities", date(2026, 8, 29), "Not Yet")
    my_task.display_info()
