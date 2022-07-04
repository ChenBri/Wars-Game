import random


class Card:

    # General testing to check if the attributes are valid
    def __init__(self, val, suite):
        self.suite = suite
        self.val = val

        # Transform `suits` into lower case
        if suite != None:
            self.suite = suite.lower()

        if self.suite not in ["diamond", "club", "heart", "spade", None]:
            raise ValueError("Suite must be a valid suite")

        if self.val < 1 or val > 14:
            raise ValueError("Val must be between 1 and 14")

        if (
            self.val == 14
            and self.suite != None
            or self.val != 14
            and self.suite == None
        ):
            raise ValueError(
                "While val is equal to 14, its suite must be None (or the other way around)"
            )

        # Capitialize the `suite`
        if self.suite != None:
            self.suite = suite.capitalize()

    def __repr__(self):
        arr = [
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
            "Ten",
            "Jack",
            "Queen",
            "King",
            "Joker!",
        ]
        if self.val != 14:
            return f"{arr[self.val-1]} of {self.suite}s"
        else:
            return f"{arr[self.val-1]}"

    def __lt__(self, other):
        return self.val < other.val

    def __gt__(self, other):
        return self.val > other.val

    def __eq__(self, other):
        return self.val == other.val


class Deck:

    # Create a new deck of cards (52 cards)
    def __init__(self):
        self.card_list = []
        for s in ["Spade", "Club", "Diamond", "Heart"]:
            for v in range(1, 14):
                self.card_list.append(Card(v, s))

        # Shuffle the deck
        random.shuffle(self.card_list)

    def draw_card(self):
        if len(self.card_list) == 0:
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
        # Reset the game, hand out new shuffled decks
        self.card_list = []
        for s in ["Spade", "Club", "Diamond", "Heart"]:
            for v in range(1, 14):
                self.card_list.append(Card(v, s))
        random.shuffle(self.card_list)

    def __repr__(self):
        return f"A Deck Containing {len(self.card_list)} Cards"

    def __lt__(self, other):
        return len(self.card_list) < len(other.card_list)

    def __gt__(self, other):
        return len(self.card_list) > len(other.card_list)

    def __eq__(self, other):
        return len(self.card_list) == len(other.card_list)


class JokerDeck(Deck):
    # Create a deck of cards including 2 Jokers (54 cards)
    def __init__(self):
        self.card_list = []
        for s in ["Spade", "Club", "Diamond", "Heart"]:
            for v in range(1, 14):
                self.card_list.append(Card(v, s))
        count = 0
        while count < 2:
            self.card_list.append(Card(14, None))
            count += 1
        random.shuffle(self.card_list)


class WarGame:
    def __init__(self, has_jokers):

        # Declaring empty variables
        self.card_pile = []
        self.d1 = []
        self.d2 = []

        if not isinstance(has_jokers, bool):
            raise TypeError("Please define the game-mode with boolean values")

        # Creating decks depending on the game mode (With or without jokers)
        if has_jokers == True:  # 54 cards each
            self.d1 = JokerDeck()
            self.d2 = JokerDeck()
        else:  # 52 cards each
            self.d1 = Deck()
            self.d2 = Deck()

    def give_pile(self, player):
        # After a player wins a round, give him the draw pile (as long as the pile isn't empty)
        if len(self.card_pile) > 0:
            if player == 1:
                self.d1.card_list += self.card_pile
                self.card_pile = []

            elif player == 2:
                self.d2.card_list += self.card_pile
                self.card_pile = []

    def round(self):
        player1Card = self.d1.draw_card()
        player2Card = self.d2.draw_card()
        print(f"Round {self.i}: {player1Card} vs {player2Card}")

        self.card_pile.append(player1Card)
        self.card_pile.append(player2Card)

        if player1Card > player2Card:
            print("Player 1 Won\n")
            self.give_pile(1)

        if player1Card < player2Card:
            print("Player 2 Won\n")
            self.give_pile(2)

        if player1Card == player2Card:
            print("War!\n.\n.\n.\n ")
            # In case one of the players can't draw 3 cards, both players will draw the maximum amount of cards he has
            # For example, if one player only has 2 cards in his hand, both players will draw 2 cards, not 3.
            if len(self.d1.card_list) < 3 or len(self.d2.card_list) < 3:
                smallerDeck = min([len(self.d1.card_list), len(self.d2.card_list)])
                self.card_pile += self.d1.draw_multiple(smallerDeck)
                self.card_pile += self.d2.draw_multiple(smallerDeck)
            # Regular situation when both players can draw 3 cards
            else:
                self.card_pile += self.d1.draw_multiple(3)
                self.card_pile += self.d2.draw_multiple(3)

    def run_game(self):
        # Number of round
        self.i = 1

        print("STARTING WAR...")
        # While both players still have cards
        while len(self.d1.card_list) > 0 and len(self.d2.card_list):
            self.round()
            self.i += 1

        if self.d1 < self.d2:
            print("PLAYER 1 IS THE VICTOR!")
        if self.d1 > self.d2:
            print("PLAYER 2 IS THE VICTOR!")
        if self.d1 == self.d2:
            print("IT'S A TIE!")


class LimitedWarGame(WarGame):
    def __init__(self, has_jokers, rounds):
        self.rounds = rounds
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

    def run_game(self):
        self.i = 1
        print("STARTING WAR...")
        while self.i < self.rounds + 1:
            self.round()
            self.i += 1

        if self.d1 < self.d2:
            print("PLAYER 1 IS THE VICTOR!")
        if self.d1 > self.d2:
            print("PLAYER 2 IS THE VICTOR!")
        if self.d1 == self.d2:
            print("IT'S A TIE!")


# game = WarGame(True)
# game = LimitedWarGame(False, 500)
# print(game.run_game())
# print(game.d1)
# print(game.d2)
