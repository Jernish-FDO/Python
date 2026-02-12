import json
from pathlib import Path

class Task:
    def __init__(self, title, category="General"):
        self.title = title
        self.category = category
        self.completed = False

    def to_dict(self):
        return self.__dict__

class TodoManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def add_task(self, title):
        new_task = Task(title)
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"✅ Added: {title}")

    def list_tasks(self):
        print("\n--- Your Tasks Buddy ---")
        for i, task in enumerate(self.tasks):
            status = "✔" if task.completed else " "
            print(f"{i}. [{status}] {task.title}")

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump([t.to_dict() for t in self.tasks], f)

    def load_tasks(self):
        if Path(self.filename).exists():
            with open(self.filename, 'r') as f:
                data = json.load(f)
                return [Task(**d) for d in data]
        return []

if __name__ == "__main__":
    manager = TodoManager()
    # Simple CLI logic
    manager.add_task("Master Python in 90 Days")
    manager.add_task("Build a cool project")
    manager.list_tasks()
