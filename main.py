from app.service import TaskService

def main():
    service = TaskService()
    service.add_task("Estudar Jenkins")
    service.add_task("Criar erros propositais")
    for task in service.list_tasks():
        print(task)

if __name__=="__main__":
    main()
    