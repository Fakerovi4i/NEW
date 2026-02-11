class Unit:

    def __init__(self, hp, name):
        self.set_hp(hp)
        self.set_name(name)

    def take_damage(self, damage=0):
        self.__hp -= damage

    def set_hp(self, hp):
        self.__hp = hp

    def get_hp(self):
        return self.__hp

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def __str__(self):
        return f"Персонаж: {self.get_name()}\nКоличество HP: {self.get_hp()}"


class Soldier(Unit):

    def __init__(self, hp, name):
        super().__init__(hp, name)

    def take_damage(self, damage=0):
        hp = self.get_hp()
        hp -= damage
        print(f"Получил {damage} урона!")
        self.set_hp(hp)
        print(f"Осталось {self.get_hp()} HP\n")


class Citizen(Unit):

    def __init__(self, hp, name):
        super().__init__(hp, name)

    def take_damage(self, damage=0):
        hp = self.get_hp()
        hp -= damage * 2
        print(f"Получил {damage} урона!")
        self.set_hp(hp)
        print(f"Осталось {self.get_hp()} HP\n")


soldier = Soldier(hp=100, name="Солдат")
print(soldier)
soldier.take_damage(damage=20)

citizen = Citizen(hp=100, name="Гражданин")
print(citizen)
citizen.take_damage(damage=20)

