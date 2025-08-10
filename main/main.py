#main.py
from task_model import task_model

def main():
    task = task_model("Estudiar para el examen")
    print(f"Tarea creada: {task.get_task_name()}")
    task.mark_as_completed()
    print(f"Tarea completada: {task.is_completed()}")

if __name__ == "__main__":
    main()