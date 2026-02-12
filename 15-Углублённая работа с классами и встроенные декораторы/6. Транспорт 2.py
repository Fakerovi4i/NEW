from abc import ABC, abstractmethod

class Transport(ABC):
    '''Абстрактный класс. Родительский класс для всего транспорта.'''

    def __str__(self) -> str:
        return (f'\nТип: {self.__class__.__name__}\n'
                f'Цвет: {self.color}')


    def __init__(self, color):
        self.color = color
        self.__speed = 0

    @abstractmethod
    def signal(self):
        pass

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed: int):
        self.__speed = speed

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color



class RadioMixin():
    radio = False

    def radio_on(self):
        print("Радио: Труляля-труляля!")



class MoveWater(ABC):
    @abstractmethod
    def move_water(self, speed):
        pass

class MoveGround(ABC):
    @abstractmethod
    def move_ground(self, speed):
        pass

class Car(Transport, MoveGround):
    def move_ground(self, speed):
        self.speed = speed
        print(f"Еду по земле со скоростью: {self.speed} km/h")

    def signal(self):
        print('Сигнал: Пииииип!')


class Boat(Transport, MoveWater):
    def move_water(self, speed):
        self.speed = speed
        print(f"Плыву со скоростью: {self.speed} узлов")

    def signal(self):
        print('Сиггнал: Тууууу!')


class Amfibia(RadioMixin, Transport, MoveWater, MoveGround):
    def __str__(self):
        return f'{super().__str__()}\nРадио: есть.'

    def move_ground(self, speed):
        self.speed = speed
        print(f"Еду по земле со скоростью: {self.speed} km/h")

    def move_water(self, speed):
        self.speed = speed
        print(f"Плыву со скоростью: {self.speed} узлов")

    def signal(self):
        print('Сигнал: Жужужу!')


car = Car('red')
boat = Boat('white')
amfib = Amfibia('blue')

for i_obj in [car, boat, amfib]:
    print(i_obj)
    if isinstance(i_obj, Car):
        i_obj.move_ground(30)
    elif isinstance(i_obj, Boat):
        i_obj.move_water(20)
    else:
        i_obj.move_water(30)
        i_obj.move_ground(40)
        i_obj.radio_on()
    i_obj.signal()

print("Новые методы!")


for i_obj in [car, boat, amfib]:
    i_obj.speed = 100
    print(i_obj.speed)
    i_obj.color = 'Синий'
    print(i_obj.color)

