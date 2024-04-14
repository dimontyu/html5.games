#Erop Sharypin, [22.03.2024 13:06]
import random
#from typing import Self


class Cards:


    @staticmethod
    def get_deck():  # Статический метод для создания колоды карт
        suits = ['♥️', '♦️', '♣️', '♠️']
        ranks = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        
        deck_sorted = [(suit, rank) for suit in suits for rank in ranks]  # Создание отсортированной колоды
        return deck_sorted

    def get_cards(self):  # Метод для раздачи карт игрокам
        for _ in range(6):  # Для каждой из 6 карт
            for player in Cards_table.players:  # Для каждого игрока
                player.set_card_in_handss(self.deck_sorted)  # Раздача карт игроку
    
    def draw_cards(players, exception_many_playear):  # Метод класса для вывода карт
        if exception_many_playear == False:
            for player in players:  # Для каждого игрока
            
                    print(f"{player.name}'s hands:")  # Выводим название игрока
                    for card in player.hands:  # Для каждой карты на руке игрока
                        print(f"\t{card}")  # Выводим карту
    
    def player_hands(self, deck):  # Метод для добавления карты в руку игрока
        self.hands = []  # Руки игрока
        cards_counter = 0  # Счетчик карт
        while deck:  # Пока колода не пуста
            cards_counter += 1  # Увеличиваем счетчик карт
            card = deck.pop()  # Достаем карту из колоды
            self.hands.append(card)  # Добавляем карту в руку игрока
            if cards_counter == 6:  # Если раздано 6 карт
                cards_counter = 0  # Сбрасываем счетчик
                break  # Прерываем цикл        
        return self.hands    
  # Раздача карт
    def distribution(deck, players, exception_many_playear):
        print("Раздача карт")
        exception_many_playear = exception_many_playear
        for player in players:  # Для каждого игрока
            player.set_card_in_hands(deck)  # Раздаем игроку карты   
            if len(deck) == 0: # Ошибка
                print("Игроков слишком много")
                exception_many_playear = True
                break


class Player:
    def __init__(self, name):  # Инициализатор класса Player
        self.name = name
    hands =  []
    
    def set_card_in_hands(self, deck):
        self.hands =  Cards.player_hands(self, deck)
        

    def get_card_in_hands(self):  # Метод для получения карт в руке
        return self.hands  # Возвращаем список карт в руке

    def draw_cards(self):  # Метод для вывода карт на руке игрока
        print(self.hands)  # Вывод карт в руке игрока
        
 
        
    def make_move(self):

        if self.hands:
            playes_card_index = random.choice(range(len(self.hands)))  # Случайным образом выбираем карту для сброса
            print(f"{self.name} ходит: {self.hands[playes_card_index]}")
            self.hands.pop(playes_card_index)  # Удаляем выбранную карту из руки игрока
        else:
            print(f"{self.name} has no cards to discard")       
                     
class Cards_table:
    
    players = [Player("Player 1"), Player("Player 2"),Player("Player 3"), Player("Player 4")]  # Создаем двух игроков
    deck = Cards.get_deck()  # Получаем колоду карт
    random.shuffle(deck)  # Перемешиваем колоду

    exception_many_playear = False 
    # Раздача карт
    Cards.distribution(deck, players, exception_many_playear )

    
    while len(deck) > 0:
        Cards.draw_cards(players,  exception_many_playear) # Вызываем метод для вывода карт на руках всех игроков
        for player in players:
            if len(player.hands) != 0: 
                player.make_move() 
            else:
                Cards.distribution(deck, players, exception_many_playear )
                break
            
         
        
                               
   #Тезисно: игроки получают на руки карты, ходят рандомной картой по очереди, как только карты у каждого заканчиваются, им выдаются новые карты и так до тех пор пока в колоде не закончатся карты