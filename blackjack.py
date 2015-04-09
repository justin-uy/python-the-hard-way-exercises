import random

class Card:
    suit = 0
    value = 0
    
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def getSuitName(self):
        names = {0: 'Clubs',
                1: 'Spades',
                2: 'Diamonds',
                3: 'Hearts'
                }

        return names[self.suit]

    def getValueName(self):
        names = {0: 'Ace',
                1: 'Two',
                2: 'Three',
                3: 'Four',
                4: 'Five',
                5: 'Six',
                6: 'Seven',
                7: 'Eight',
                8: 'Nine',
                9: 'Ten',
                10: 'Jack',
                11: 'Queen',
                12: 'King'
                }

        return names[self.value]

    def getFullName(self):
        return '%s of %s' % (self.getValueName(), self.getSuitName())

class BlackjackHand:
    cards = []
    handValue = 0
    
    def __init__(self, card1, card2):
        
        for card in [card1, card2]:
            self.addCard(card)

    def hasBlackjack(self):
        return len(self.cards) == 5 or self.handValue == 21
    
    def addCard(self, card):
        
        if card.value == 0:
            if (self.handValue + 11 <= 21):
                self.handValue += 11
            else:
                self.handValue += 1

        elif card.value > 8:
            self.handValue += 10
        else:
            self.handValue += (card.value + 1)
        
        self.cards.append(card)

    def isBust(self):
       return self.handValue > 21
    
    def getHandString(self):
        
        cardNames = []

        for card in self.cards:
            cardNames.append(card.getFullName())

        return ' '.join(cardNames)

class Deck:
    cards = []

    def __init__(self):
        for suit in range(0,4):
            for value in range (0,13):
                self.cards.append(Card(suit,value))
        
        self.shuffle()

    def shuffle(self):
        
        for i in range(0, len(self.cards)):
            self.swapCards(i,random.randint(0,len(self.cards)))
        

    def swapCards(self,i1,i2):
        tmp = self.cards[i1]
        self.cards[i1] = self.cards[i2]
        self.cards[i2] = tmp

    def deal(self):
        return self.cards.pop()

hand = BlackjackHand(Card(0,0),Card(1,0))

print hand.handValue
print hand.getHandString()

deck = Deck()

for card in deck.cards:
    print card.getFullName()

