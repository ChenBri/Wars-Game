import random


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
        return self.val > other.val


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
            self.card_list = self.card_list[1:] + [self.card_list[0]]
            return self.card_list

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



    
test = Deck()
test2 = Deck()
test.draw_multiple(5)

print(test>test2)


    