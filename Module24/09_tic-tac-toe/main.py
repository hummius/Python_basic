class Cell:
    def __init__(self, number):
        self.number = number
        self.busy = False
        self.what = ''


class Board:
    positions_dict = {'X':[], 'O':[]}

    def __init__(self):
        self.board = [Cell(number) for number in range(1, 10)]

    def view_of_board(self):
        for cell in self.board:
            if cell.number % 3 != 0:
                if cell.busy:
                    print(f'{cell.what}', end='  |  ')
                else:
                    print(' ', end ='  |  ')
            if cell.number % 3 == 0:
                if cell.busy:
                    print(f'{cell.what}')
                else:
                    print(' ', end='')
                    print()
                if cell.number != 9:
                    print('--------------\n', end='')

    def winner_check(self, curplayer, positions=positions_dict):
        solution = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],
                    [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        for i in solution:
            if all(j in positions[curplayer.symbol] for j in i):
                return True

    def tie_check(self, positions=positions_dict):
        if len(positions['X']) + len(positions['O']) == 9:
            return True

class Player:
    def __init__(self, name):
        self.name = name
        self.cell = 0
        self.symbol = ''

    def move(self):
        for cell in game_board.board:
                if cell.number == self.cell:
                    if not cell.busy:
                        cell.busy = True
                        cell.what = self.symbol
                        Board.positions_dict[self.symbol].append(cell.number)
                    else:
                        print('Эта клетка уже занята.')


def start_game(player_1, player_2):
    game_board.view_of_board()
    while True:
        try:
            command_1 = int(input(f'На какую клетку ходит {player_1.name}? (1-9) '))
            if command_1 < 1 or command_1 > 9:
                raise ValueError
            else:
                player_1.cell = command_1
                player_1.move()
                game_board.view_of_board()
                if game_board.winner_check(player_1):
                    print(f'\n{player_1.name} выиграл!')
                    break
                if game_board.tie_check():
                    print('\nНичья!')
                    break

                command_2 = int(input(f'На какую клетку ходит {player_2.name}? (1-9) '))
                if command_2 < 1 or command_2 > 9:
                    raise ValueError
                else:
                    player_2.cell = command_2
                    player_2.move()
                    game_board.view_of_board()
                    if game_board.winner_check(player_2):
                        print(f'\n{player_1.name} выиграл!')
                        break
                    if game_board.tie_check():
                        print('\nНичья!')
                        break

        except ValueError:
            print('\nОшибка: не верная команда.')
        if game_board.tie_check():
            print('\nНичья!')
            break

game_board = Board()
player_1 = Player(input('Введите имя: '))
player_1.symbol = 'X'
player_2 = Player(input('Введите имя: '))
player_2.symbol = 'O'
start_game(player_1, player_2)
