class Robots:

    def __init__(self, model):
        self.model = model

    def operate(self):
        print(f"{self.model} выполняет операцию: ", end="")


class Cleaner(Robots): #Можно дописать функцию для заполнения и опустошения мешка, но по заданию не требуется

    def __init__(self, model):
        super().__init__(model)
        self.bag = 0

    def operate(self):
        super().operate()
        print(f"Пылесосит...(заполненность мешка: {self.bag})\n")

class Warrior(Robots):

    def __init__(self, model, gun):
        super().__init__(model)
        self.gun = gun

    def operate(self):
        super().operate()
        print(f"Защищает объект...(оружие: {self.gun})", end =" ")

class Submarine(Warrior):

    def __init__(self, model, gun, deph):
        super().__init__(model, gun)
        self.deph = deph

    def operate(self):
        print("\n")
        super().operate()
        print(f"(глубина: {self.deph})")


cleaner = Cleaner("Xiaomi Air")
warrior = Warrior("T-2030", "Сдвоенные пулеметы 50-го калибра")
sub = Submarine("Каракатица-1020", "Торпеды", 50)

cleaner.operate()
warrior.operate()
sub.operate()

