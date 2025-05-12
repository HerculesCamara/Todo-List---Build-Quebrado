class Task:
    def __init__(self, title)
        self.title = title
        self.done = False
    

    def complete(self):
        self.done = True


    def __str__(self):
        status = "✔" if self.done else "✘"
        return f"[{status}] {self.title}"