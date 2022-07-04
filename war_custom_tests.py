from war_cards_chen_brilling import *

# game = WarGame(True)
# game = LimitedWarGame(False, 500)
# print(game.run_game())
# print(game.d1)
# print(game.d2)

# Card Class:
# print(Card(5, "HeArT"))
# print(Card(14, None))
# print(Card(14, "Spade"))
# print(Card(1, None))
# print(Card(16, "diamond"))
# print(Card(1, "bla"))
# print(Card(1, "diamond") > Card(2, "diamond"))
# print(Card(3, "diamond") < Card(2, "diamond"))
# print(Card(14, None) == Card(14, None))

# Deck Class:
# print(Deck().card_list)
# print(Deck().draw_card())
# print(Deck().draw_multiple(5))
# print(Deck().draw_multiple(55))
# print(Deck())
# print(Deck().shuffle())
# print(Deck().reset())
# print(Deck())
# print(Deck() > Deck())
# print(Deck() < Deck())
# print(Deck() == Deck())

# JokerDeck Class:
# print(JokerDeck())
# print(JokerDeck().card_list)

# WarGame Class:
# var = WarGame(True)
# # print(var.d1)
# # print(var.d2)
# # print(var.d1 == var.d2)
# print(var.round(1))
# print(var.round(5))
# print(var.run_game())
# print(var.d1)
# print(var.d2)

# LimitedWarGame Class:
# var = LimitedWarGame(True, 1)
# var = LimitedWarGame(True, 10)
# var = LimitedWarGame(True, 100)
# var = LimitedWarGame(True, 1000)
# var = LimitedWarGame(True, 10000)
# var = LimitedWarGame(True, 100000)


var = LimitedWarGame(True, 55)
print(var.run_game())
