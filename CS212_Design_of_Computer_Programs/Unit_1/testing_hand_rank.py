# -----------
# User Instructions
# 
# Modify the test() function to include three new test cases.
# These should assert that card_ranks gives the appropriate
# output for the given straight flush, four of a kind, and
# full house.
#
# For example, calling card_ranks on sf should output  
# [10, 9, 8, 7, 6]
#
# Since the program is still incomplete, clicking RUN won't do 
# anything, but clicking SUBMIT will let you know if you
# have gotten the problem right. 

# -----------
# User Instructions
# 
# Modify the card_ranks() function so that cards with
# rank of ten, jack, queen, king, or ace (T, J, Q, K, A)
# are handled correctly. Do this by mapping 'T' to 10, 
# 'J' to 11, etc...

def card_ranks(cards):
	"Return a list of the ranks, sorted with higher first."
	ranks = [r for r,s in cards]
	i = 0
	while i < len(ranks):
		str_r = str(ranks[i])
		if str_r == 'T':
			ranks[i] = 10
		elif str_r == 'J':
			ranks[i] = 11
		elif str_r == 'Q':
			ranks[i] = 12
		elif str_r == 'K':
			ranks[i] = 13
		elif str_r == 'A':
			ranks[i] = 14

		ranks[i] = int(ranks[i])

		i = i + 1
		
	ranks.sort(reverse=True)
	return ranks

print card_ranks(['AC', '3D', '4S', 'KH']) #should output [14, 13, 4, 3]

def test():
    "Test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([sf]) == sf
    assert poker([sf] + 99*[fh]) == sf
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]
    return 'tests pass'

