import random

###
# Card Class
###

class Card:
    
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

###
# Hane Class
###

class BlackjackHand:
    
  def __init__(self, card1, card2):
    
    self.cards = []
    self.handValue = 0

    for card in [card1, card2]:
        self.addCard(card)

  @staticmethod
  def getWinningHand(hand1, hand2):
    if (hand1.getHandValue() <= 21) and ((hand1.getHandValue() > hand2.getHandValue()) or (hand2.getHandValue() > 21)):
      return hand1
    elif (hand2.getHandValue() <= 21) and ((hand2.getHandValue() > hand1.getHandValue()) or (hand1.getHandValue() > 21)):
      return hand2

    return None

  def getFirstCardString(self):
    return self.cards[0].getFullName()

  def getHandValue(self):
    return self.handValue

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

    return ', '.join(cardNames)

###
# Deck Class
###

class Deck:

  def __init__(self):

    self.cards = []

    for suit in range(0,4):
      for value in range (0,13):
        self.cards.append(Card(suit,value))
      
    self.shuffle()

  # iterate through the deck and swap the card at each index with another card at a random index
  def shuffle(self):
      
    for i in range(0, len(self.cards) - 1):
        self.swapCards(i,random.randint(0,len(self.cards) - 1))
      

  def swapCards(self,i1,i2):
    tmp = self.cards[i1]
    self.cards[i1] = self.cards[i2]
    self.cards[i2] = tmp


  def deal(self):
    return self.cards.pop()


##
# Game Functions
##

def printHandAndTotal(name, hand):
  print name
  print hand.getHandString()
  print hand.getHandValue()


def startGame():
  
  deck = Deck()
  
  playerHand = BlackjackHand(deck.deal(), deck.deal())
  dealerHand = BlackjackHand(deck.deal(), deck.deal())

  playerDone = False

  print '\nThe Game has begun: Blackjack'

  printHandAndTotal('you: ', playerHand)

  # show one of the dealers cards
  print '\ndealer: '
  print dealerHand.getFirstCardString()

  while (not playerDone):
    print '\nWould you like another card?'
    action = raw_input()

    if (action == 'hitme'):
      playerHand.addCard(deck.deal())
      printHandAndTotal('\nyou', playerHand) 
    elif (action == 'nope'):
      playerDone = True
    else:
      print 'that made no sense!'
    
    if (playerHand.isBust() or playerHand.hasBlackjack()):
      print 'you are done, whether you like it or not!'
      playerDone = True
  
  # if player busts, dealer wins
  #
  # if player does not bust, dealer will draw until above or bust
  #
  # if dealer bust, player wins
  #
  # if dealer does not bust then dealer wins

  while (not playerHand.isBust()) and (not dealerHand.isBust()) and (dealerHand.getHandValue() <= playerHand.getHandValue()):

    dealerHand.addCard(deck.deal())

  winner = BlackjackHand.getWinningHand(playerHand, dealerHand)

  printHandAndTotal('\n\nyou', playerHand)
  printHandAndTotal('dealer', dealerHand)

  if (playerHand == winner):
    print '\nyou win!'
  else:
    print '\nbetter luck next time!'

startGame()

