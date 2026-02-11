
class Human:
    __counter = 0

    def __init__(self, name, age):
        self.set_name(name)
        # self.set_age(age)
        self.__age = age
        self.__counter += 1

    def set_name(self, name):
        if name.isalpha():
            self.__name = name
        else:
            raise Exception("Имя содержит не только буквы!")

    def set_age(self, age):
        if not isinstance(age, int):
            raise Exception("Возраст должен содержать только целое число!")
        elif not age in range(0, 100):
            raise Exception("Возраст должен быть в диапазоне 0 - 100!")
        else:
            self.__age = age

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def __str__(self):
        res = (f"Количество людей: {self.__counter}\n"
               f"Имя: {self.__name}\n"
               f"Возраст: {self.__age}\n")
        return res



human_1 = Human("Volodea", 99)
# human_1.set_name("Vanea")
# human_1.set_age(33)
human_1._Human__counter = 40    #Тут агресивно меняем данные (так делать не надо)
human_1._Human__age = 40    #Тут агресивно меняем данные (так делать не надо)
print(human_1)
print(human_1.get_name())