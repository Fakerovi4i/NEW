import random
def random_speed():
    return random.randint(0, 200)

class Toyota:
    color = 'red'
    price = 1000000
    max_speed = 200
    current_speed = 0
#Нарисовал 2 метода
    def info(self):
        print(
            f"Color: {self.color}\n"
            f"Price: {self.price}\n"
            f"Max Speed: {self.max_speed}\n"
            f"Current speed: {self.current_speed}\n"
        )

    def cur_speed(self, input_speed):
        self.current_speed = input_speed
        print(f"Current speed is changed to {input_speed} km/h\n")


car_1 = Toyota()
car_2 = Toyota()
car_3 = Toyota()

car_1.current_speed = random_speed()#Рандомно накидываю значения текущей скорости
car_2.current_speed = random_speed()
car_3.current_speed = random_speed()

car_1.cur_speed(199)#Проверка работы метода

car_1.info()
car_2.info()
car_3.info()