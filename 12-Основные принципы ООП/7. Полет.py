class CanFly:
    def __init__(self):
        self._height = 0
        self._speed = 0

    def takeoff(self):
        pass

    def flying(self):
        pass

    def landing(self):
        self._height, self._speed = 0, 0

    def info(self):
        print(f"Высота: {self._height}")
        print(f"Скорость: {self._speed}")


class Butterfly(CanFly):

    def takeoff(self):
        self._height = 1

    def flying(self):
        self._speed = 0.5

class Rocket(CanFly):

    def takeoff(self):
        self._height = 500
        self._speed = 1000

    def landing(self):
        super().landing()
        self.__explosion()

    def __explosion(self):
        print("БДЫЩ!!!!")


print("Бабочка:")
butterfly = Butterfly()
butterfly.info()
butterfly.takeoff()
butterfly.flying()
butterfly.info()

print("\nРакета:")
rocket = Rocket()
rocket.info()
rocket.takeoff()
rocket.info()
rocket.landing()
rocket.info()
