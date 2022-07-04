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