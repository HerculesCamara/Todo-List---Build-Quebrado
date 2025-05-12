from app.services import TaskService

def test_add_and_list_tasks():
    service = TaskService()
    service.add_task("Tarefa 1")
    tasks = service.list_tasks()
    assert len(tasks) == 2
    ## assert tasks[0].title == "Tarefa 1"
