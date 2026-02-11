class Robot:
    def init(self, name='Обычный робот.'):
        self.name = name

    def operate(self):
        print('\nЯ - робот!')


class CanFly:
    def init(self):
        self.height = 0
        self.speed = 0

    def takeoff(self):
        print("\nВзлетаю!")

    def flying(self):
        pass

    def landing(self):
        print('Приземляюсь...')
        self.height, self.speed = 0, 0
        print(f"Скорость: {self.speed}, Высота {self.height}")


class ReconDron(Robot, CanFly):
    def init(self, name='Разведывательный дрон'):
        super().init(name)

    def operate(self):
        print()
        print(f'{self.name}: Веду разведку с воздуха!')
        self.flying()

    def flying(self):
        print('\nПередвигаюсь...')


class MilitaryDron(Robot, CanFly):
    def init(self, name='\nВоенный дрон'):
        super().init(name)
        self.gun = "Пушка"

    def operate(self):
        print(f'{self.name}: Защищаю объект с воздуха! Оружие: {self.gun}')


recon = ReconDron()
recon.operate()
robot = Robot()
robot.operate()
military = MilitaryDron()
military.operate()
print(recon.


class .mro)
recon.takeoff()
recon.landing()