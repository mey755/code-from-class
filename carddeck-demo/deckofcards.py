# 52 cards
# 4 suits
# A, 2-10, Jack, Queen, King

import random 

class CardDeck():
    #build the deck
    suits = ["Hearts", "Clubs", "Spades", "Diamonds"]
    values = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven","Eight", "Nine", "Ten", "Jack", "Queen", "King"]

    def __init__(self):
        self.deck = []
        for suit in self.suits:
            for value in self.values:
                self.deck.append([value, suit])


    #shuffle
    def  shuffleDeck(self):
        for i in range(1000):
            random.shuffle(self.deck)


    #deal a card
    def dealCard(self):
        return self.deck.pop()

    #display the deck
    def displayDeck(self):
        for card in self.deck:
            print(card)

def main():
    theDeck = CardDeck()
    # print(theDeck)
    # theDeck.displayDeck()
    players = [[], [], [], []]
    # print()
    theDeck.shuffleDeck() #does not display only shuffles the deck of cards
    # print()
    # theDeck.displayDeck()
    players.append([])
    players.append([])
    players.append([])
    players.append([]) 
    for i in range(13):
     # print(f" Card dealt: {theDeck.dealCard()}")
            players[0].append(theDeck.dealCard())
            players[1].append(theDeck.dealCard())
            players[2].append(theDeck.dealCard())
            players[3].append(theDeck.dealCard())

    count = 0
    for player in players:
        print(f"Player {count}")
        for card in player:
            print(card)

        count += 1


main()