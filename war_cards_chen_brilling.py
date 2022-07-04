import random
from threading import get_native_id

class Card:
    def __init__(self, val, suite):
        self.suite = suite
        self.val = val

        if suite != None:
            self.suite = suite.lower()

        if self.suite not in ['diamond', 'club', 'heart', 'spade', None]:
            raise ValueError("Suite must be a valid suite")
    
        if self.val < 1 or val > 14:
            raise ValueError("Val must be between 1 and 14")
        
        if self.val == 14 and self.suite != None or self.val!=14 and self.suite==None:
            raise ValueError("While val is equal to 14, his suite must be None")  

        if self.suite != None:
           self.suite = suite.capitalize() 
        
    def __repr__(self):
        arr = ['One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Joker!']
        if self.val !=14:
            return f'{arr[self.val-1]} of {self.suite}s'
        else:
            return f'{arr[self.val-1]}'
        
    def __lt__(self, other):
        return self.val < other.val

    def __gt__(self, other):
        return self.val > other.val

    def __eq__(self, other):
        return self.val == other.val


class Deck:
    def __init__(self):
        self.card_list = []
        for s in ['Spade', 'Club', 'Diamond', 'Heart'] :
                for v in range (1 , 14) :
                     self.card_list.append(Card(v , s))
        random.shuffle(self.card_list)            

    def __repr__(self):
        return str(self.card_list)

    def draw_card(self):
        if len(self.card_list)==0:
            return None
        else:
            firstCard = self.card_list.pop(0)
            return firstCard

    def draw_multiple(self, num):
        throwenCards = []

        if len(self.card_list) < num:
            return None
        else:
            throwenCards = self.card_list[:num]
            self.card_list = self.card_list[num:]
            return throwenCards

    def shuffle(self):
        random.shuffle(self.card_list)
        return self.card_list

    def reset(self):
        self.card_list = []
        for s in ['Spade', 'Club', 'Diamond', 'Heart'] :
                for v in range (1 , 14) :
                     self.card_list.append(Card(v , s))
        random.shuffle(self.card_list)

    def __repr__(self):
        return f'A Deck Containing {len(self.card_list)} Cards'

    def __lt__(self, other):
        return len(self.card_list) > len(other.card_list)

class JokerDeck(Deck):
         def __init__(self):
            self.card_list = []
            for s in ['Spade', 'Club', 'Diamond', 'Heart'] :
                    for v in range (1 , 14) :
                        self.card_list.append(Card(v , s))
            count = 0
            while count < 2:
                self.card_list.append(Card(14 , None))
                count+=1
            random.shuffle(self.card_list)
          
class WarGame:
    def __init__(self, has_jokers):
        self.card_pile = []
        self.d1 = []
        self.d2 = []

        if not isinstance(has_jokers, bool):
            raise TypeError("Please define the game-mode with boolean values")

        if has_jokers == True:
            self.d1 = JokerDeck()
            self.d2 = JokerDeck()
        else:
            self.d1 = Deck()
            self.d2 = Deck()
        
        
    def give_pile(self, player):
        if len(self.card_pile) > 0:
            if player==1:
                self.d1.card_list += self.card_pile
                self.card_pile = []
                
                
            elif player==2:
                self.d2.card_list += self.card_pile
                self.card_pile = []

            

    def round (self, i):
        player1Card = self.d1.draw_card()
        player2Card = self.d2.draw_card()
        print(f'Round {i}: {player1Card} vs {player2Card}')

        self.card_pile.append(player1Card)
        self.card_pile.append(player2Card)

        if player1Card > player2Card:
            print('Player 1 Won\n')
            self.give_pile(1)

        if player1Card < player2Card:
            print('Player 2 Won\n')
            self.give_pile(2)

        if player1Card == player2Card:
            print('War!\n.\n.\n.\n ')
            self.card_pile += self.d1.draw_multiple(3)
            self.card_pile += self.d2.draw_multiple(3)

        


test = WarGame(False)
print(test.d1)
print(test.d2)
print(test.round(1))
print(test.d1)
print(test.d2)
print(test.card_pile)

