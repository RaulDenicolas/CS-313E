#  File: Poker.py

#  Description: Use object oriented programming to simulate a regular Poker game otherwise known as the 5-Card Draw.

#  Student Name: Raul Denicolas

#  Course Name: CS 313E

#  Unique Number: 52038

#  Date Created: 1/ 9/ 2023

#  Date Last Modified: 1/ 12/ 2023

import sys, random

class Card (object):
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

  SUITS = ('C', 'D', 'H', 'S')

  # constructor
  def __init__ (self, rank = 12, suit = 'S'):
    if (rank in Card.RANKS):
      self.rank = rank
    else:
      self.rank = 12

    if (suit in Card.SUITS):
      self.suit = suit
    else:
      self.suit = 'S'

  # string representation of a Card object
  def __str__ (self):
    if (self.rank == 14):
      rank = 'A'
    elif (self.rank == 13):
      rank = 'K'
    elif (self.rank == 12):
      rank = 'Q'
    elif (self.rank == 11):
      rank = 'J'
    else:
      rank = str (self.rank)
    return rank + self.suit

  # equality tests
  def __eq__ (self, other):
    return self.rank == other.rank

  def __ne__ (self, other):
    return self.rank != other.rank

  def __lt__ (self, other):
    return self.rank < other.rank

  def __le__ (self, other):
    return self.rank <= other.rank

  def __gt__ (self, other):
    return self.rank > other.rank

  def __ge__ (self, other):
    return self.rank >= other.rank

class Deck (object):
  # constructor
  def __init__ (self, num_decks = 1):
    self.deck = []
    for i in range (num_decks):
      for suit in Card.SUITS:
        for rank in Card.RANKS:
          card = Card (rank, suit)
          self.deck.append (card)

  # shuffle the deck
  def shuffle (self):
    random.shuffle (self.deck)

  # deal a card
  def deal (self):
    if (len(self.deck) == 0):
      return None
    else:
      return self.deck.pop(0)

class Poker (object):
  # constructor
  def __init__ (self, num_players = 2, num_cards = 5):
    self.deck = Deck()
    self.deck.shuffle()
    self.players_hands = []
    self.numCards_in_Hand = num_cards

    # deal the cards to the players
    for i in range (num_players):
      hand = []
      for j in range (self.numCards_in_Hand):
        hand.append (self.deck.deal())
      self.players_hands.append (hand)

  # simulate the play of poker
  def play (self):
    # sort the hands of each player and print
    for i in range (len(self.players_hands)):
      sorted_hand = sorted (self.players_hands[i], reverse = True)
      self.players_hands[i] = sorted_hand
      hand_str = ''
      for card in sorted_hand:
        hand_str = hand_str + str (card) + ' '
      print ('Player ' + str(i + 1) + ' : ' + hand_str)
    # determine the type of each hand and print
    hand_type = []	# create a list to store type of hand
    hand_points = []
    type_of_hand = []

    # determine winner and print
    print('')
    for i in range (len(self.players_hands)):
      sorted_hand = sorted (self.players_hands[i], reverse = True)
      self.players_hands[i] = sorted_hand
      test_hand = []
      for card in sorted_hand:
        test_hand.append(card)
      hand_type = self.is_royal(test_hand)
      if hand_type[0] == 0:
        hand_type = self.is_straight_flush(test_hand)
        if hand_type[0] == 0:
          hand_type = self.is_four_kind(test_hand)
          if hand_type[0] == 0:
            hand_type = self.is_full_house(test_hand)
            if hand_type[0] == 0:
              hand_type = self.is_flush(test_hand)
              if hand_type[0] == 0:
                hand_type = self.is_straight(test_hand)
                if hand_type[0] == 0:
                  hand_type = self.is_three_kind(test_hand)
                  if hand_type[0] == 0:
                    hand_type = self.is_two_pair(test_hand)
                    if hand_type[0] == 0:
                      hand_type = self.is_one_pair(test_hand)
                      if hand_type[0] == 0:
                        hand_type = self.is_high_card(test_hand)
      type_of_hand.append(hand_type[1])
      hand_points.append(hand_type[0])
      #hand_points[str(i+1)] = str(hand_type)
      print ('Player ' + str(i + 1) + ': ' + str(hand_type[1]))

    print()
    max_score = max(hand_points)
    score_list = []
    for i in hand_points:
      score_list.append(i)
    #print(score_list)
    #print(type_of_hand)
    #print(max_score)

    place = score_list.index(max_score)
    winning_type_of_hand = type_of_hand[place]
    #print(winning_type_of_hand)
    #print('Player ' + str(place+1) + ' wins.')

    type_of_hand[place] = ''
    #print(type_of_hand)
    if winning_type_of_hand not in type_of_hand:
      print('Player ' + str(place+1) + ' wins.')
    if winning_type_of_hand in type_of_hand:
      print('Player ' + str(place+1) + ' ties.')
      while winning_type_of_hand in type_of_hand:
        holder = type_of_hand.index(winning_type_of_hand)
        print('Player ' + str(int(type_of_hand.index(winning_type_of_hand))+1) + ' ties.')
        type_of_hand[holder] = ''

  # determine if a hand is a royal flush
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  def is_royal (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return 0, ''

    rank_order = True
    for i in range (len(hand)):
      rank_order = rank_order and (hand[i].rank == 14 - i)

    if (not rank_order):
      return 0, ''

    points = 10 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'Royal Flush'

  def is_straight_flush (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)
    if (not same_suit):
      return 0, ''
    
    rank_order = True
    for i in range (len(hand) - 1):
      rank_order = rank_order and (hand[i].rank == (hand[i + 1].rank + 1))
    for i in range (len(hand) - 1):
      if (hand[i].rank == 14):
        return 0, ''
    
    points = 9 * 15**5 + hand[0].rank * 15**4 + hand[1].rank * 15**3 + hand[2].rank * 15**2 + hand[3].rank * 15 + hand[4].rank

    
    return points, 'Straight Flush'

  def is_four_kind (self, hand):
    four_kind = False
    for i in range(0, len(hand)-3):
      if hand[i].rank == hand[i+3].rank:
        hand.insert(0, hand.pop(i))
        hand.insert(1, hand.pop(i+1))
        hand.insert(2, hand.pop(i+2))
        hand.insert(3, hand.pop(i+3))
        four_kind = True
    if (not four_kind):
      return 0, ''

    points = 8 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)
    return points, 'Four of a Kind'

  def is_full_house (self, hand):
    full_house = False
    if (hand[0].rank == hand[1].rank) and (hand[3].rank == hand[4].rank):
      if (hand[2].rank == hand[0].rank):
        full_house = True
      elif (hand[2].rank == hand[4].rank):
        hand.insert(0, hand.pop(2))
        hand.insert(1, hand.pop(3))
        hand.insert(2, hand.pop(4))
        full_house = True
    if (not full_house):
      return 0, ''
    
    points = 7 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)
    return points, 'Full House'

  def is_flush (self, hand):
    flush = True
    for i in range (len(hand) - 1):
      if hand[i].suit != hand[0].suit:
        flush = False
        break
    if (not flush):
      return 0, ''
    
    points = 6 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)
    return points, 'Flush'

  def is_straight (self, hand):
    straight = False
    count = 0
    for i in range (len(hand) - 1):
      if hand[i + 1].rank == hand[i].rank - 1:
        count += 1
    if count == 4:
      straight = True
    if (not straight):
      return 0, ''

    points = 5 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)
    return points, 'Straight'

  def is_three_kind (self, hand):
    three_kind = False
    for i in range(0, len(hand)-2):
      if hand[i].rank == hand[i+2].rank:
        hand.insert(0, hand.pop(i))
        hand.insert(1, hand.pop(i+1))
        hand.insert(2, hand.pop(i+2))
        three_kind = True
    if (not three_kind):
      return 0, ''

    points = 4 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)
    return points, 'Three of a Kind'

  def is_two_pair (self, hand):
    hand.reverse()
    two_pair = False
    pair_count = 0
    for i in range (len(hand) - 1):
      if (hand[i].rank == hand[i + 1].rank):
        pair_count += 1
        hand.insert(0, hand.pop(i))
        hand.insert(1, hand.pop(i+1))
    if pair_count == 2:
      two_pair = True
    if (not two_pair):
      return 0, ''

    points = 3 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)
    return points, 'Two Pair'

  # determine if a hand is one pair
  # takes as argument a list of 5 Card objects
  # returns the number of points for that hand
  def is_one_pair (self, hand):
    one_pair = False
    for i in range (len(hand) - 1):
      if (hand[i].rank == hand[i + 1].rank):
        hand.insert(0, hand.pop(i))
        hand.insert(1, hand.pop(i+1))
        one_pair = True
        break
    if (not one_pair):
      return 0, ''

    points = 2 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)
    return points, 'One Pair'

  def is_high_card (self,hand):
    points = 1 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)
    return points, 'High Card'

def main():
  # read number of players from stdin
  line = sys.stdin.readline()
  line = line.strip()
  num_players = int (line)
  if (num_players < 2) or (num_players > 6):
    return

  print('Number of players:', num_players)
  print()
  # create the Poker object
  game = Poker (num_players)

  # play the game
  game.play()

if __name__ == "__main__":
  main()
