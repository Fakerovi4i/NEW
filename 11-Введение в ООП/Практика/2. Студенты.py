from random import randint

class Student:
    def __init__(self, name):
        self.name = name
        self.n_group = randint(1, 3)
        self.progress = [randint(2, 5) for _ in range(5)]

    def mid_progress(self):
        return sum(self.progress) / len(self.progress)

    def info(self):
        return f"{self.name}, Группа: {self.n_group}, Оценки: {self.progress}, Средний балл: {self.mid_progress()}"

names = ('Александр Иванов, Мария Конева, Иван Сонов, Елена Анатольевна, Дмитрий Дюжев, '
         'Ольга Бузова, Сергей Есенин, Анна Кондратов, Андрей Панин, Наталья Сюткина').split(", ")

student_list = [Student(i) for i in names]

student_list.sort(key=lambda val_for_sort: val_for_sort.mid_progress())

for i in student_list:
    print(i.info())