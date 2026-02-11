class Hero:
    # Базовый класс, который не подлежит изменению
    # У каждого наследника будут атрибуты:
    # - Имя
    # - Здоровье
    # - Сила
    # - Жив ли объект
    # Каждый наследник будет уметь:
    # - Атаковать
    # - Получать урон
    # - Выбирать действие для выполнения
    # - Описывать своё состояние

    max_hp = 150
    start_power = 10

    def __init__(self, name):
        self.name = name
        self.__hp = self.max_hp
        self.__power = self.start_power
        self.__is_alive = True

    def get_hp(self):
        return self.__hp

    def set_hp(self, new_value):
        self.__hp = max(new_value, 0)

    def get_power(self):
        return self.__power

    def set_power(self, new_power):
        self.__power = new_power

    def is_alive(self):
        return self.__is_alive

    # Все наследники должны будут переопределять каждый метод базового класса (кроме геттеров/сеттеров)
    # Переопределенные методы должны вызывать методы базового класса (при помощи super).
    # Методы attack и __str__ базового класса можно не вызывать (т.к. в них нету кода).
    # Они нужны исключительно для наглядности.
    # Метод make_a_move базового класса могут вызывать только герои, не монстры.
    def attack(self, target):
        # Каждый наследник будет наносить урон согласно правилам своего класса
        pass

    def take_damage(self, damage):
        # Каждый наследник будет получать урон согласно правилам своего класса
        # При этом у всех наследников есть общая логика, которая определяет жив ли объект.
        print("\t", self.name, "Получил удар с силой равной = ", round(damage), ". Осталось здоровья - ", round(self.get_hp()))
        # Дополнительные принты помогут вам внимательнее следить за боем и изменять стратегию, чтобы улучшить выживаемость героев
        if self.get_hp() <= 0:
            self.__is_alive = False

    def make_a_move(self, friends, enemies):
        # С каждым днём герои становятся всё сильнее.
        self.set_power(self.get_power() + 0.1)

    def __str__(self):
        return f"[{type(self).__name__}] Имя: {self.name} | HP: {round(self.get_hp(), 2)} "

class Healer(Hero):
    # Целитель:
    # Атрибуты:
    # - магическая сила - равна значению НАЧАЛЬНОГО показателя силы умноженному на 3 (self.__power * 3)
    def __init__(self, name):
        super().__init__(name)
        self.__magic_power = self.start_power * 3

    # Методы:
    # - атака - может атаковать врага, но атакует только в половину силы self.__power
    def attack(self, target):
        target.take_damage(self.get_power() / 2)

    # - получение урона - т.к. защита целителя слаба - он получает на 20% больше урона (1.2 * damage)
    def take_damage(self, damage):
        damage = damage * 1.2
        self.set_hp(self.get_hp() - damage)
        super().take_damage(damage)

    # - исцеление - увеличивает здоровье цели на величину равную своей магической силе
    def heal(self, target):
        target.set_hp(target.get_hp() + self.__magic_power)

    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
    # исцеление) на выбранную им цель
    def make_a_move(self, friends, enemies):
        if self.get_hp() <= 90:
            print(f"У меня мало хп: {self.get_hp()}, лечу себя.")
            self.heal(self)
            print(f"HP после лечения: {self.get_hp()}")
        else:
            friends_to_heal = [i_friend for i_friend in friends
                               if i_friend != self and i_friend.get_hp() < 130]
            if friends_to_heal:  # Проверка на пустой список
                min_hp_friend = min(friends_to_heal, key=lambda fnd: fnd.get_hp())
                print(f"У {min_hp_friend.name} мало HP ({min_hp_friend.get_hp()}). Лечу")
                self.heal(min_hp_friend)
            else:
                min_hp_enemies = min(enemies, key=lambda enms: enms.get_hp())
                print(f"С HP у всех все хорошо. Атакую {min_hp_enemies.name}.")
                self.attack(min_hp_enemies)
        super().make_a_move(friends, enemies)
    

class Tank(Hero):
    # Танк:
    # Атрибуты:
    # - показатель защиты - изначально равен 1, может увеличиваться и уменьшаться
    # - поднят ли щит - танк может поднимать щит, этот атрибут должен показывать поднят ли щит в данный момент
    def __init__(self, name):
        super().__init__(name)
        self._armor = 1
        self.shield_up = False

    # Методы:
    def attack(self, target):
        target.take_damage(self.get_power() / 2)
        # - атака - атакует, но т.к. доспехи очень тяжелые - наносит половину урона (self.__power)
    def take_damage(self, damage):
        damage = damage / self._armor
        self.set_hp(self.get_hp() - damage)
        super().take_damage(damage)
    # - получение урона - весь входящий урон делится на показатель защиты (damage/self.defense) и только потом отнимается от здоровья

    def raise_shield(self):
        self.shield_up = True
        self._armor *= 2
        self.set_power(self.get_power() / 2)
    # - поднять щит - если щит не поднят - поднимает щит. Это увеличивает показатель брони в 2 раза, но уменьшает показатель силы в 2 раза.

    def put_down_shield(self):
        self.shield_up = False
        self._armor /= 2
        self.set_power(self.get_power() * 2)
    # - опустить щит - если щит поднят - опускает щит. Это уменьшает показатель брони в 2 раза, но увеличивает показатель силы в 2 раза.

    def make_a_move(self, friends, enemies):
        min_hp_enemies = min(enemies, key=lambda enms: enms.get_hp())
        if self.get_hp() <= 120 and not self.shield_up:
            print("ХП меньше 120. Поднимаю щит.")
            self.raise_shield()
        elif self.get_hp() > 120 and self.shield_up:
            if min_hp_enemies.get_hp() + 0.1 <= self.get_power() / 2:
                print("ХП достаточно. Могу добить.")
                self.attack(min_hp_enemies)
            else:
                print("ХП достаточно опускаю щит")
                self.put_down_shield()
        else:
            print("ХП достаточно. Атакую.")
            self.attack(min_hp_enemies)
        super().make_a_move(friends, enemies)

    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
    # поднять щит/опустить щит) на выбранную им цель


class Attacker(Hero):
    # Убийца:
    # Атрибуты:
    def __init__(self, name):
        super().__init__(name)
        self.__multiply = 2
    # - коэффициент усиления урона (входящего и исходящего)

    # Методы:
    # - атака - наносит урон равный показателю силы (self.__power) умноженному на коэффициент усиления урона (self.power_multiply)
    def attack(self, target):
        target.take_damage(self.get_power() * self.__multiply)
        self.power_down()
        # после нанесения урона - вызывается метод ослабления power_down.

    def take_damage(self, damage):
        # - получение урона - получает урон равный входящему урона умноженному на половину коэффициента усиления урона - damage * (
        # self.power_multiply / 2)
        damage = damage * (self.__multiply / 2)
        self.set_hp(self.get_hp() - damage)
        super().take_damage(damage)

    def power_up(self):
        # - усиление (power_up) - увеличивает коэффициента усиления урона в 2 раза
        self.__multiply *= 2

    def power_down(self):
        # - ослабление (power_down) - уменьшает коэффициента усиления урона в 2 раза
        self.__multiply /= 2

    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
    # усиление, ослабление) на выбранную им цель
    def make_a_move(self, friends, enemies):
        max_hp_enemies = max(enemies, key=lambda enms: enms.get_hp())
        if self.__multiply > 4:
            print(f"У меня коэффициент {self.__multiply} > 4, "
                  f"атакую монстра с максимальным хп")
            self.attack(max_hp_enemies)
        elif self.get_hp() > 100 and self.__multiply < 3:
            print(f"Усиление! HP {self.get_hp()}. Коеффициент: {self.__multiply}")
            self.power_up()
        else:
            berserk_list = [i_enemy for i_enemy in enemies if type(i_enemy).__name__ == "MonsterBerserk"]
            if berserk_list:
                print("Атакую берсерка!")
                min_berserk = min(berserk_list, key=lambda enms: enms.get_hp())
                self.attack(min_berserk)
            else:
                sort_enemies = sorted(enemies, key=lambda enms: enms.get_hp(), reverse=True)
                print("Берсерков нет. Атакую монстра с мин ХП")
                for i_enemy in sort_enemies:
                    if (self.get_power() * self.__multiply) >= i_enemy.get_hp():
                        self.attack(i_enemy)
                        break






