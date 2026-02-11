class Potato:
    states = {0: "Картошки нет", 1: "Росток", 2: "Зеленая", 3: "Зрелая"}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def print_state(self):
        print(f"Картошка {self.index} сейчас {Potato.states[self.state]};")

    def is_ripe(self):
        if self.state == 3:
            return True
        return False


class PotatoGarden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count+1)]

    def grow_all(self):
        print("Картошка прорастает!")
        for i_potato in self.potatoes:
            i_potato.grow()

    def all_is_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print("Картошка еще не созрела!\n")
        else:
            print("Вся картошка на грядке созрела! Можно собирать!\n")


first_garden = PotatoGarden(2)
first_garden.all_is_ripe()

for _ in range(3):
    first_garden.grow_all()
    first_garden.all_is_ripe()














