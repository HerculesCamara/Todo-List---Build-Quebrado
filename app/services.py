from app.modelos import Task

class TaskService:
    
    def __init__(self):
        self.tasks = []

    
    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)


    def list_tasks(self):
        return self.tasks
    

    def complete_task(self, index):
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Ìndice Inválido")
        self.tasks[index].complete()