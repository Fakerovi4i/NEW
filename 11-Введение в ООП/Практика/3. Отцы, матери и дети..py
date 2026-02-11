

class Parent:
    def __init__(self, name, age, kid_list):
         self.name = name
         self.age = age
         self.kid_list = kid_list
         for i in self.kid_list:
             if (self.age - i.age) < 16:
                 raise ValueError(f"{i.name} младше родителя менее чем на 16 лет")


    def info(self):
        name_kid_list = [
            f"[{i_name.name}: {i_name.age} лет, {i_name.states_info()}]"
            for i_name in self.kid_list]
        name_kids_str = ", ".join(name_kid_list)
        return (f"Имя родителя: {self.name}\n"
                f"Возраст родителя: {self.age}\n"
                f"Дети: {name_kids_str}")

    def calm_kid(self, name_kid):
        for i_kid in self.kid_list:
            if i_kid.name == name_kid:
                i_kid.state_calm = 1

    def eat_kid(self, name_kid):
        for i_kid in self.kid_list:
            if i_kid.name == name_kid:
                i_kid.state_hungry = 1


class Kid:
    states_hungry = {1: "Сыт", 2: "Голоден"}
    states_calm = {1: "Спокоен", 2: "Плачет"}

    def __init__(self, name='unnamed', age=10):
        self.name = name
        self.age = age
        self.state_calm = 1
        self.state_hungry = 1
    def states_info(self):
        return f"{self.states_calm[self.state_calm]} и {self.states_hungry[self.state_hungry]}"


kids = [Kid("Ваня", 13), Kid("Аня", 15)]
parent = Parent("Саша", 30, kids)
print(parent.info())

#Проверки
kids[1].state_hungry, kids[1].state_calm = 2, 2
kids[0].state_hungry = 2


print(parent.info())

parent.calm_kid("Аня")
parent.eat_kid("Ваня")

print(parent.info())














