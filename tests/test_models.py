from app.models import Task

def test_task_creation():
    task = Task("Testar Jenkins")
    assert task.title == "Testar Jenkins"
    assert not task.done

def test_task_completion():
    task = Task("Finalizar testes")
    task.complete()
    assert task.done
