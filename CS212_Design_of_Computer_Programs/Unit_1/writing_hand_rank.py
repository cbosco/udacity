# -----------
# User Instructions
# 
# Modify the hand_rank function so that it returns the
# correct output for the remaining hand types, which are:
# full house, flush, straight, three of a kind, two pair,
# pair, and high card hands. 
# 
# Do this by completing each return statement below.
#
# You may assume the following behavior of each function:
#
# straight(ranks): returns True if the hand is a straight.
# flush(hand):     returns True if the hand is a flush.
# kind(n, ranks):  returns the first rank that the hand has
#                  exactly n of. For A hand with 4 sevens 
#                  this function would return 7.
# two_pair(ranks): if there is a two pair, this function 
#                  returns their corresponding ranks as a 
#                  tuple. For example, a hand with 2 twos
#                  and 2 fours would cause this function
#                  to return (4, 2).
# card_ranks(hand) returns an ORDERED tuple of the ranks 
#                  in a hand (where the order goes from
#                  highest to lowest rank). 
#
# Since we are assuming that some functions are already
# written, this code will not RUN. Clicking SUBMIT will 
# tell you if you are correct.

def poker(hands):
    "Return the best hand: poker([hand,...]) => hand"
    return max(hands, key=hand_rank)

def hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
		# your code here
		return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):                              # flush
		# your code here
        return (5, ranks)
    elif straight(ranks):                          # straight
		# your code here
        return (4, max(ranks))
    elif kind(3, ranks):                           # 3 of a kind
		# your code here
		return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):                          # 2 pair
		# your code here
		return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):                           # kind
		# your code here
		return (1, kind(2, ranks), ranks)
    else:                                          # high card
		# your code here
		return (0, ranks)

def test():
	"Test cases for the functions in poker program"
	sf = "6C 7C 8C 9C TC".split() # Straight Flush
	fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
	fh = "TD TC TH 7C 7D".split() # Full House
	# new hands
	flush		= "7C 8C 9C TC AC".split() # Flush
	straight	= "7C 8H 9C TC JD".split() # Straight
	threekind	= "TD TC TH 3C 7D".split() # Three of a kind
	twopair		= "TD TC 8H 3C 3D".split() # Two pair
	twokind		= "TD TC 8H 3C 2D".split() # Two of a kind
	highcard	= "TD 8H 5C 3C 2D".split() # High card only
	assert poker([sf, fk, fh]) == sf
	assert poker([fk, fh]) == fk
	assert poker([fh, fh]) == fh
	assert poker([sf]) == sf
	assert poker([sf] + 99*[fh]) == sf
	assert hand_rank(sf) == (8, 10)
	assert hand_rank(fk) == (7, 9, 7)
	assert hand_rank(fh) == (6, 10, 7)
	# new tests
	assert poker([straight, threekind]) == straight
	assert hand_rank(flush) == (5, 14, 10, 9, 8, 7)
	assert hand_rank(straight) == (4, 11)
	assert hand_rank(threekind) == (3, 10, 7)
	assert hand_rank(twopair) == (2, 10, 3, 8)
	assert hand_rank(twokind) == (1, 10, 8, 3, 2)
	assert hand_rank(highcard) == (0, 10, 8, 5, 3, 2)

	return 'tests pass'
