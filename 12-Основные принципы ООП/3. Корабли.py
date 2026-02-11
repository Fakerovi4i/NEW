class Ship:

    def __init__(self, model):
        self.model = model

    def __str__(self):
        return (f"Молдель коробля: {self.model}")

    def sail(self):
        print("Корабль плывет.")


class Warship(Ship):

    def __init__(self, model, gun):
        super().__init__(model)
        self.gun = gun

    def atacking(self):
        print("Атакую!")

class Cargoship(Ship):

    def __init__(self, model):
        super().__init__(model)
        self.conteiner = 0

    def load(self):
        self.conteiner += 1
        print("Загружаем")
        print("Заполненность:", self.conteiner)

    def unload(self):
        if self.conteiner > 0:
            self.conteiner -= 1
            print("Разгружаем!")
        else:
            print("Корабль уже разгружен!")
        print("Заполненность:", self.conteiner)





warship = Warship("Eagle-2010", "Корабельное орудие")
print(warship)
warship.sail()
warship.atacking()

cargo_ship = Cargoship("Геркулес")
print(cargo_ship)
cargo_ship.load()
cargo_ship.sail()
cargo_ship.unload()
cargo_ship.unload()

