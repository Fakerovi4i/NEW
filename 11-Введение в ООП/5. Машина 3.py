import random
def random_speed():
    return random.randint(0, 200)

class Toyota:

    def __init__(self, color='yellow', price=1000000, max_speed=200, current_speed=0):
        self.color = color#'red'
        self.price = price#1000000
        self.max_speed = max_speed#200
        self.current_speed = current_speed#0

    # #Нарисовал 2 метода
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

car_1 = Toyota(color='red', current_speed=random_speed())
car_2 = Toyota(price=500000, current_speed=random_speed())
car_3 = Toyota(max_speed=220, current_speed=100)
car_4 = Toyota(color='Black')
car_4.cur_speed(80)

car_1.info()
car_2.info()
car_3.info()
car_4.info()
