import random

class Card:

    def __init__(self, number, suit):
        if number < 11:
            self.rang = number
            self.value = number
        elif number == 11:
            self.rang = 'Валет'
            self.value = 10
        elif number == 12:
            self.rang = 'Дама'
            self.value = 10
        elif number == 13:
            self.rang = 'Король'
            self.value = 10
        elif number == 14:
            self.rang = 'Туз'
            self.value = 11
        self.suit = suit


class Deck:

    def __init__(self):
        self.deck_of_cards = [Card(number, suit) for suit in ['Пики', 'Червы', 'Бубны', 'Трефы']
                              for number in range(2, 15)]
    deck_of_used = set()
    def used_deck(self, deck_of_used=deck_of_used):
        if self in deck_of_used:
            return True
        else:
            deck_of_used.add(self)
            return False

class Player:

    def __init__(self, name):
        self.name = name
        self.cards_list = []
        self.cards_list = self.take_a_card(2)

    def print_cards(self):
        print(f'\n{self.name} карты на руках:')
        for card in self.cards_list:
            print('     ', card.rang, card.suit)

    def take_a_card(self, count=1):
        temp = list()
        while count != 0:
            card_to_take = (random.choice(game_cards.deck_of_cards))
            if Deck.used_deck(card_to_take):
                continue
            else:
                print(f'Рука {self.name}а тянется и берет карту из колоды')
                temp.append(card_to_take)
                count -= 1
        if temp:
            return temp

    def score_check(self):
        full_sum = 0
        for info in self.cards_list:
            if info.rang == 'Туз' and full_sum > 21:
                full_sum += 1
            else:
                full_sum += info.value
        return full_sum

def start_game():
    while True:
        player_1.print_cards()
        comp_player.print_cards()

        if comp_player.score_check() >= 21 or player_1.score_check() >= 21:
            break
        else:
            action = input('\nЖелаете взять карту или нет? (да/нет) ').lower()
            if action == 'да':
                player_1.cards_list.extend(player_1.take_a_card())
                if comp_player.score_check() <= 14:
                    comp_player.cards_list.extend(comp_player.take_a_card())
            elif action == 'нет':
                if player_1.score_check() > comp_player.score_check():
                    comp_player.cards_list.extend(comp_player.take_a_card())
                    player_1.print_cards()
                    comp_player.print_cards()
                break
            else:
                print('Ошибка: неверная команда.')

def who_is_winner(player_1, player_2):
    a = player_2.score_check()
    b = player_1.score_check()
    if a > 21 and b <= 21:
        print(f'\n{player_1.name} выиграл! {player_2.name} проиграл!')
    elif a <= 21 and b > 21:
        print(f'\n{player_1.name} проиграл! {player_2.name} выиграл!')
    elif a > b:
        print(f'\n{player_1.name} проиграл! {player_2.name} выиграл!')
    elif a < b:
        print(f'\n{player_1.name} выиграл! {player_2.name} проиграл!')
    else:
        print('Ничья!')

game_cards = Deck()
player_1 = Player(input('Введите имя игрока: '))
comp_player = Player('Компьютер')
start_game()
who_is_winner(player_1, comp_player)