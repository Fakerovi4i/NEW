class Board:
    def __init__(self):
        self.cells_list = [Cell(index) for index in range(1, 10)] #Тут индекс клеток от 1, но список с 0

    def is_change_state_cell(self, num_cell): #Проверяет занята ли клетка
        if self.cells_list[num_cell-1].state_free:
            self.cells_list[num_cell-1].state_free = False
            return True
        return False

    def isWin(self):#Переименовать на ISWIN, метод проверяет победу
        combine_win_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],
            [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        for i_comb in combine_win_list:
            symbols = [self.cells_list[i-1].symbol for i in i_comb]
            if symbols == ['X', "X", "X"] or symbols == [0, 0, 0]:
                return True
        return False

    def isFin(self):
        if all([not i_cell.state_free for i_cell in self.cells_list]):
            return True
        return False


class Cell:

    def __init__(self, index):
        self.num_of_cell = index
        self.state_free = True
        self.symbol = None

class Player:

    def __init__(self, name):
        self.name = name
        self.num_win = 0

    def move(self):
        print(self.name, 'сделайте ваш ход (1-9): ', end='')
        p_move = int(input())
        return p_move


class Game:

    def __init__(self):
        self.state_game = True
        self.players_list = [Player(f'Player_№{num_player}') for num_player in (1, 2)]
        self.board = Board()

    def one_move(self, player):
        print('Новый ход:')
        while True:
            p_move = player.move()
            if not self.board.is_change_state_cell(p_move):#Еще сделать проверку от 1 до 9 чтоб игрок вводил
                print("Клетка занята! Попробуйте еще раз.")
            else:
                if player.name == "Player_№1":
                    self.board.cells_list[p_move - 1].symbol = "X"
                else:
                    self.board.cells_list[p_move - 1].symbol = 0
                    print()
            return self.board.isWin()


    def one_game(self):
        print("Игра началась!\n")
        self.board = Board()
        while self.state_game:
            for i_player in self.players_list:
                if self.one_move(i_player):
                    print(f"\nПОБЕДИЛ {i_player.name}!")
                    i_player.num_win += 1
                    self.state_game = False
                    return True
                elif self.board.isFin():
                    print("НИЧЬЯ!")
                    self.state_game = False
                    return True
        return False

    def main(self):
        self.one_game()
        while True:
            print(f"Текущий счет:\n"
                  f"{self.players_list[0].name}: {self.players_list[0].num_win}\n"
                  f"{self.players_list[1].name}: {self.players_list[1].num_win}\n"
                  )
            while True:
                choice = int(input("Хотите продолжить?(1-да, 2-нет): "))
                if choice == 2:
                    print("Конец игры.")
                    return
                elif choice == 1:
                    self.state_game = True
                    self.one_game()
                    break
                elif choice != 1:
                    print("Введите 1 или 2.")


new_game = Game()

new_game.main()
















