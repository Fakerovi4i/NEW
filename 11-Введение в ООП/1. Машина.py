import random
def random_speed():
    return random.randint(0, 200)
class Tayota:
    color = 'red'
    price = 1000000
    max_speed = 200
    current_speed = 0

car_1 = Tayota()
car_2 = Tayota()
car_3 = Tayota()

car_1.current_speed = random_speed()
car_2.current_speed = random_speed()
car_3.current_speed = random_speed()

print(f'car_1: {car_1.color}, {car_1.price}, {car_1.max_speed}, {car_1.current_speed}')
print(f'car_2: {car_2.color}, {car_2.price}, {car_2.max_speed}, {car_2.current_speed}')
print(f'car_3: {car_3.color}, {car_3.price}, {car_3.max_speed}, {car_3.current_speed}')
