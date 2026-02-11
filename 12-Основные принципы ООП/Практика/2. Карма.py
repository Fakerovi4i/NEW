import random
class KillError(Exception):
    def __init__(self):
        super().__init__("KillError")
class DrunkError(Exception):
    def __init__(self):
        super().__init__("DrunkError")
class CarCrashError(Exception):
    def __init__(self):
        super().__init__("CarCrashError")
class GluttonyError(Exception):
    def __init__(self):
        super().__init__("GluttonyError")
class DepressionError(Exception):
    def __init__(self):
        super().__init__("DepressionError")


def one_day():
    if random.randint(1, 10) == 1:
        exc_choice = random.choice(exception_tuple)
        raise exc_choice()
    return random.randint(1, 7)

exception_tuple = (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError)
karma_need = 500
karma = 0

with open("karma.log", 'w') as open_file:
    while karma < karma_need:
        try:
            karma += one_day()
        except exception_tuple as e:
            open_file.write(f'{e}\n')

print(f"Набрано нужное количество кармы!\n"
      f"Карма: {karma}")
