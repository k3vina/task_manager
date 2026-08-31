from datetime import date

class Task:

    def __init__(self, id, title, description, due_date, completed, priority):
        self.id = id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = completed
        self.priority = priority

    
    def display_info(self):
        print(f"id: {self.id}")
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Date: {self.due_date}")
        print(f"Completed: {self.completed}")
        print(f"Priority: {self.priority}")

    def to_row(self):
        return f"{self.id:^10}, {self.title:<20}, {self.description:<50}, {self.due_date:^15}, {self.completed:^10}, {self.priority:^10}"

    def header_row(self):
        return f'{"Id":^10}, {"Title":<20}, {"Description":<50}, {"Date":^15}, {"Completed":^10}, {"Priority":^10}'

if __name__ == "__main__":
    my_task = Task("1", "To-Do List", "Today's activities", date(2026, 8, 29), "Not Yet", "High")
    my_task.display_info()
