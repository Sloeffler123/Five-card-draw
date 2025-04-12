import random

cards = [(2,'hearts'),(3,'hearts'),(4,'hearts'),(5,'hearts'),(6,'hearts'),(7,'hearts'),(8,'hearts'),(9,'hearts'),(10,'hearts'),(11,'hearts'),(12,'hearts'),(13,'hearts'),(14,'hearts'),(2,'diamonds'),(3,'diamonds'),(4,'diamonds'),(5,'diamonds'),(6,'diamonds'),(7,'diamonds'),(8,'diamonds'),(9,'diamonds'),(10,'diamonds'),(11,'diamonds'),(12,'diamonds'),(13,'diamonds'),(14,'diamonds'),(2,'clubs'),(3,'clubs'),(4,'clubs'),(5,'clubs'),(6,'clubs'),(7,'clubs'),(8,'clubs'),(9,'clubs'),(10,'clubs'),(11,'clubs'),(12,'clubs'),(13,'clubs'),(14,'clubs'),(2,'spades'),(3,'spades'),(4,'spades'),(5,'spades'),(6,'spades'),(7,'spades'),(8,'spades'),(9,'spades'),(10,'spades'),(11,'spades'),(12,'spades'),(13,'spades'),(14,'spades'),]

class Player:
    def __init__(self,name,balance,big_blind=False,small_blind=False):
        self.name = name 
        self.balance = balance
        self.big_blind = False
        self.small_blind = False
        self.cards = self.get_cards(cards)
    def get_cards(self,deck):
        self.player_cards_lst = []
        self.readable_player_hand = []
        for i in range(5):
            rand_card = random.choice(cards)
            self.player_cards_lst.append(rand_card)
            if rand_card[0] > 10:
                self.change_card_values(rand_card)
            else:
                self.readable_player_hand.append(rand_card)                        
            cards.remove(rand_card)
        self.player_cards_lst.sort()  
        # self.readable_player_hand.sort()

    def swap(self,card,suit):
        rand_card = random.choice(cards)
        self.readable_player_hand.remove((card,suit))
        match card:
            case 11:
                self.player_cards_lst.remove((11,suit))
                self.readable_player_hand.append(('Jack', rand_card[1]))
            case 12:
                self.player_cards_lst.remove((12,suit))
                self.readable_player_hand.append(('Queen', rand_card[1]))
            case 13:
                self.player_cards_lst.remove((13,suit))
                self.readable_player_hand.append(('King', rand_card[1]))
            case 14:
                self.player_cards_lst.remove((14,suit))
                self.readable_player_hand.append(('Ace', rand_card[1]))             
        self.player_cards_lst.append((rand_card)) 
    def change_card_values(self,random_card):
            
            match random_card[0]:
                case 11:
                    self.readable_player_hand.append(('Jack', random_card[1]))
                case 12:
                    self.readable_player_hand.append(('Queen', random_card[1]))
                case 13:
                    self.readable_player_hand.append(('King', random_card[1]))
                case 14:
                    self.readable_player_hand.append(('Ace', random_card[1]))
    def __str__(self):
        return f'{self.name}'                

player_1 = Player('sam',1000)       #maybe check if the player big blind is odd or small is even
player_2 = Player('bob',1000)
player_3 = Player('larry',1000)
player_4 = Player('garry',1000)
player_list = [player_1,player_2,player_3,player_4]
def player_hand(player):
    print(f'YOUR HAND: {player}')
    for i in player.readable_player_hand:
        print(f'{i[0]}, {i[1]}')

def card_swap(player):
    print('What cards would you like to swap? ')
    card, suit = input('Card:'), input('Suit: ')
    player.swap(card, suit)

def get_bet(player):
    try:
        player_bet = int(input(f'{player} how much would you like to bet? '))
        if player_bet > player.balance:
            raise Exception('Bet exceeds total balance')
        else:
            player.balance -= player_bet
    except ValueError:
        print('Please enter a valid input')
        
def order_of_blinds(list_players):
    big = list_players[0]
    small = list_players[1]
    big.big_blind = True
    small.small_blind = False
    list_players.pop(big)
    list_players.append(big)
        
game = True

while game:
    order = []
    for i in player_list:
        player_hand(i)
        if len(order) == 2:
            order.append(player_list[1])
        elif len(order) == 3:
            order.append(player_list[0])    
        else:
            order.append(i)
        input('press enter when done')    
    # bet
    print(order)
    for player in order:
        get_bet(player)

