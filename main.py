import random

cards = []

for j in range(2,15):
    cards.append((j, 'hearts'))
    cards.append((j, 'clubs'))
    cards.append((j, 'diamonds'))
    cards.append((j, 'spades'))
print(len(cards))    

class Player:
    def __init__(self,name,balance,blind=None):
        self.name = name 
        self.balance = balance
        self.cards = self.get_cards(cards)
    def get_cards(self,deck):
        self.player_cards_lst = []
        self.readable_player_hand = []
        for i in range(5):
            rand_card = random.choice(cards)
            self.player_cards_lst.append(rand_card)
            if rand_card[0] > 10:
                match rand_card:
                    case 11:
                        self.readable_player_hand.append(('Jack', rand_card[1]))
                    case 12:
                        self.readable_player_hand.append(('Queen', rand_card[1]))
                    case 13:
                        self.readable_player_hand.append(('King', rand_card[1]))
                    case 14:
                        self.readable_player_hand.append(('Ace', rand_card[1]))
            else:
                self.readable_player_hand.append([rand_card,rand_card])                        
            cards.remove(rand_card)
        self.player_cards_lst.sort()  
        self.readable_player_hand.sort()

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
player_1 = Player('sam',1000,'big')
player_2 = Player('bob',1000,'small')

def player_1_hand():
    print(f'YOUR HAND:')
    for i in player_1.readable_player_hand:
        print(f'{i[0]}: {i[1]}')

def player_2_hand():
    print(f'YOUR HAND:')
    for i in player_2.readable_player_hand:
        print(f'{i[0]}: {i[1]}')

def card_swap(player):
    print('What cards would you like to swap? ')
    card, suit = input('Card:'), input('Suit: ')
    player.swap(card, suit)
    







game = True


# num = 1
# def main():
#     while game is True:
#         #after players have seen there cards make the big blind and little blinds
        
#         if num < num_players:
