from random import randint

class Unit:
    def __init__(self, name='Воин'):
        self.name = name
        self.hp = 100

    def damage(self):
        if self.hp > 0:
            self.hp -= 20

    def info_hp(self):
        print(f"У {self.name} отсалось {self.hp} здоровья!\n")

    def is_dead(self):
        if self.hp <= 0:
            return True
        return False

def battle(un_1, un_2):
    un_2.damage()
    print(f"Атакует {un_1.name}")
    if not un_2.is_dead():
        un_2.info_hp()
        return False
    else:
        return True



unit_1 = Unit("Воин_1")
unit_2 = Unit("Воин_2")

while True:
    if randint(1, 2) == 1:
        if battle(unit_1, unit_2):
            print(f"Победил {unit_1.name}!")
            break

    else:
        if battle(unit_2, unit_1):
            print(f"Победил {unit_2.name}!")
            break



