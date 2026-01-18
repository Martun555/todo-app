class Task:
    def __init__(self, title):
        self.title = title
        self.done = False

    def __str__(self):
        status = "✓" if self.done else "✗"
        return f"[{status}] {self.title}"


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        self.tasks.append(Task(title))
        print("Задача добавлена")

    def show_tasks(self):
        if not self.tasks:
            print("Список пуст")
            return
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            print("Задача удалена")
        else:
            print("Неверный номер")

    def mark_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].done = True
            print("Задача выполнена")
        else:
            print("Неверный номер")

    def save_to_file(self):
        with open("tasks.txt", "w", encoding="utf-8") as f:
            for task in self.tasks:
                f.write(f"{task.title}|{task.done}\n")

    def load_from_file(self):
        try:
            with open("tasks.txt", "r", encoding="utf-8") as f:
                for line in f:
                    title, done = line.strip().split("|")
                    task = Task(title)
                    task.done = done == "True"
                    self.tasks.append(task)
        except FileNotFoundError:
            pass


todo = TodoList()
todo.load_from_file()

while True:
    print("\n--- TO-DO OOP ---")
    print("1 - Показать задачи")
    print("2 - Добавить задачу")
    print("3 - Удалить задачу")
    print("4 - Отметить выполненной")
    print("0 - Выход")

    choice = input("Ваш выбор: ")

    if choice == "1":
        todo.show_tasks()
    elif choice == "2":
        title = input("Введите задачу: ")
        todo.add_task(title)
        todo.save_to_file()
    elif choice == "3":
        todo.show_tasks()
        index = int(input("Номер задачи: ")) - 1
        todo.delete_task(index)
        todo.save_to_file()
    elif choice == "4":
        todo.show_tasks()
        index = int(input("Номер задачи: ")) - 1
        todo.mark_done(index)
        todo.save_to_file()
    elif choice == "0":
        print("Пока 👋")
        break
    else:
        print("Неверный выбор")
