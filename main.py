tasks = []


def show_tasks():
    if not tasks:
        print("Список задач пуст")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def add_task():
    task = input("Введите задачу: ")
    tasks.append(task)
    print("Задача добавлена")


def delete_task():
    show_tasks()
    if not tasks:
        return
    number = int(input("Введите номер задачи для удаления: "))
    if 1 <= number <= len(tasks):
        tasks.pop(number - 1)
        print("Задача удалена")
    else:
        print("Неверный номер")


while True:
    print("\n--- TO-DO LIST ---")
    print("1 - Показать задачи")
    print("2 - Добавить задачу")
    print("3 - Удалить задачу")
    print("0 - Выход")

    choice = input("Ваш выбор: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "0":
        print("До свидания 👋")
        break
    else:
        print("Неверный выбор")
