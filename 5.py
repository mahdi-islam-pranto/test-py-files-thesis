# File: todo_list.py

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def display_tasks(self):    #ggwp
        print("Tasks:")
        
        for index, task in enumerate(self.tasks, 1):
            print(f"{index}. {task}")

class Newclass2:
    def new2(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.remove(task)

# Usage example:
# Tasks:
# 1. Buy groceries
# 2. Go to the gym