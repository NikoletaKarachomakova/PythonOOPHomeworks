from ToDoList.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        tasks_names = [t.name for t in self.tasks]
        if task_name not in tasks_names:
            return f"Could not find task with the name {task_name}"

        index = tasks_names.index(task_name)
        current_task = self.tasks[index]
        current_task.completed = True
        return f"Completed task {task_name}"

    def clean_section(self):
        list_competed = [t for t in self.tasks if t.completed]
        count_completed_tasks = len(list_competed)
        while True:
            if len(list_competed) == 0:
                break
            current_task = list_competed.pop()
            self.tasks.remove(current_task)
        return f"Cleared {count_completed_tasks} tasks."

    def view_section(self):
        result = f"Section {self.name}:\n"
        for t in self.tasks:
            result += f"{t.details()}\n"
        return result
