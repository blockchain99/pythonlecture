
# Your goal in this exercise is to implement two classes, 
# Card  and Deck .

# Specifications

# Card 

# Each instance of Card  should have a suit 
#   ("Hearts", "Diamonds", "Clubs", or "Spades").
# Each instance of Card  should have a value 
#   ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K").
# Card 's __repr__  method should return the card's value and suit 
#   (e.g. "A of Clubs", "J of Diamonds", etc.)

# Deck 

# Each instance of Deck  should have a cards attribute with 
# all 52 possible instances of Card .
# Deck  should have an instance method called count  
# which returns a count of how many cards remain in the deck.
# Deck 's __repr__  method should return information on 
# how many cards are in the deck 
# (e.g. "Deck of 52 cards", "Deck of 12 cards", etc.)
# Deck  should have an instance method called _deal  
# which accepts a number and removes at most that many cards 
# from the deck (it may need to remove fewer 
# if you request more cards than are currently in the deck!).
#  If there are no cards left, this method should return 
# a ValueError  with the message "All cards have been dealt".
# Deck  should have an instance method called shuffle  
# which will shuffle a full deck of cards. 
# If there are cards missing from the deck, 
# this method should return a ValueError  
# with the message "Only full decks can be shuffled".  
# shuffle should return the shuffled deck.
# Deck  should have an instance method called deal_card  
# which uses the _deal  method to deal a single card 
# from the deck and return that single card.
# Deck  should have an instance method called deal_hand  
# which accepts a number and uses the _deal  method 
# to deal a list of cards from the deck and return that list of cards.
from random import shuffle
class Card:
   
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"


c = Card("A", "Hearts") 
c2 = Card("10","Diamonds")
c3 = Card("K", "Spades")
print(c,c2,c3) #with __repr__ shows output phrase. 
print(c.suit)
print(c.__repr__()) 



class Deck:    
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs","Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        # self.card = []
        # # Card('A', "Hearts") #shows value suit pair by __repr__
        # for suit in suits:
        #     for value in values:
        #         # print(Card( value, suit))
        #         self.card.append(Card(value, suit))

        self.cards = [Card(value, suit) for suit in suits for value in values]
        print(self.cards)
    
    def __repr__(self):
        return f"Deck of {self.count()} cards"
    
    def count(self):
        return len(self.cards)

    def _deal(self, num):
        count = self.count()
        actual = min([count, num])
        if count == 0:
            raise ValueError("All cards have been dealt")
        cards = self.cards[-actual:] #slicing out
        self.cards = self.cards[:-actual] #update after slice out
        return cards
    def deal_card(self): #del one card
        return self._deal(1)[0]
    
    def deal_hand(self, hand_size):
        return self._deal(hand_size)
    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
    
print("------------- instanciate Card-----------")
d = Deck()
print(d.count()) #52 

print("-------after _repr_ added ----------")
d = Deck()
##instead of d.count() _. instantiated,d show result using __repr__
print(d) 
# d.cards.pop()
d._deal(5)
print(d)

print("=====")
print(d._deal(3)) #by print() return cards -> we can see!!
print(d.count())

print("------- check all cards not any more ----")
d = Deck()
print(d._deal(52))
print(d.count())
# print(d._deal(3)) #error

print("---------shuffle ----------")
d=Deck()
d.shuffle()
print(d)
print("------")
print(d.cards)


   
