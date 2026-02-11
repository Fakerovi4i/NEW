from random import randint

class Human:
    def __init__(self, name, home):
        self.name = name
        self.home = home
        self.sotiety = 50
        self.is_alive = True

    def check_alive(self):
        if self.sotiety <= 0:
            self.is_alive = False
        return self.is_alive


    def eat(self):
        if self.home.food >= 10:
            self.home.food -= 10
            self.sotiety += 10
            print(f"{self.name} - поел!")
            return True
        print(f"{self.name} - не смог поесть (нет еды)!")
        return False

    def work(self):
        self.home.money += 50
        self.sotiety -= 10
        print(f"{self.name} поработал. Всего денег в доме: {self.home.money}")


    def go_to_magazine(self):
        if self.home.money >= 50:
            self.home.money -= 50
            self.home.food += 50
            print(f"{self.name} сходил в магазин. Сейчас еды: {self.home.food}")
            return True
        print(f"{self.name} не смог купить еды. Мало денег!")
        return False


    def play(self):
        self.sotiety -= 10
        print(f"{self.name}: Поиграл.")


    def live_one_day(self):
        if not self.check_alive():
            return False
        num_cube = randint(1, 6)

        if self.sotiety < 20:
            print(f"{self.name}: Пытаюсь поесть!")
            if not self.eat():
                print("Не смог поесть! Попробую в магазин!")
                self.go_to_magazine()
            return True
        elif self.home.food < 10:
            print(f"{self.name}: Мало еды, попробую пойти в магазин!")
            self.go_to_magazine()
            return True
        elif self.home.money < 50:
            print(f"{self.name}: Мало денег, пойду на работу!")
            self.work()
            return True
        elif num_cube == 1:
            print(f"{self.name}: Выпал кубик '1', пойду на работу!")
            self.work()
            return True
        elif num_cube == 2:
            print(f"{self.name}: Выпал кубик '2', пойду поем!")
            self.eat()
            return True
        else:
            print(f"{self.name}: Делать нечего буду играть!")
            self.play()
            return True

class House:
    def __init__(self):
        self.food = 50
        self.money = 0

sweet_home = House()

alex = Human("Alex", sweet_home)
jim = Human("Jim", sweet_home)

for i in range(1, 366):
    print(f"-========== День {i}-й ==========-\n")

    if not alex.live_one_day():
        print("Алекс Умер!")
        break

    if not jim.live_one_day():
        print("Джим Умер!")
        break

    print(f"\nРесурсы: Еда - {sweet_home.food}, Деньги - {sweet_home.money}")
    print(f"Алекс: Сытость - {alex.sotiety}")
    print(f"Джим: Сытость - {jim.sotiety}\n")

else:
    print("Все прошло успешно!")