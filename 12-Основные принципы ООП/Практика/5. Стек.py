class Stack:
    def __init__(self):
        self.__lst = []

    def __str__(self):

        return "; ".join(self.__lst)

    def add_elem(self, elem):
        self.__lst.append(elem)

    def pop_elem(self):
        if len(self.__lst) == 0:
            return None
        return self.__lst.pop()

class TaskManager:
    def __str__(self):
        display = []
        if self.__tasks:
            for i_prior in sorted(self.__tasks.keys()):
                display.append(
                    f"{str(i_prior)} - {self.__tasks[i_prior]}\n"
                )
        return "".join(display)

    def __init__(self):
        self.__tasks = dict()

    def new_task(self, task, priority):
        if priority not in self.__tasks:
            self.__tasks[priority] = Stack()
        self.__tasks[priority].add_elem(task)






manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать ДЗ", 2)
print(manager)
# Результат:
# 1 — отдохнуть
# 2 — поесть; сдать ДЗ
# 4 — сделать уборку; помыть посуду

