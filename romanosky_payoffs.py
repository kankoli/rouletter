import lib.utils as utils

"""
Template Roulette Table

+---+----+----+----+----+----+----+----+----+----+----+----+----+------+
|   |  3 |  6 |  9 | 12 | 15 | 18 | 21 | 24 | 27 | 30 | 33 | 36 | 2to1 |
|   |----+----+----+----+----+----+----+----+----+----+----+----+------+
| 0 |  2 |  5 |  8 | 11 | 14 | 17 | 20 | 23 | 26 | 29 | 32 | 35 | 2to1 |
|   |----+----+----+----+----+----+----+----+----+----+----+----+------+
|   |  1 |  4 |  7 | 10 | 13 | 16 | 19 | 22 | 25 | 28 | 31 | 34 | 2to1 |
+---+----+----+----+----+----+----+----+----+----+----+----+----+------+
    |     1st Dozen     |     2nd Dozen     |     3rd Dozen     |
    +---------+---------+---------+---------+---------+---------+
    |   1-18  |   Even  |   Red   |  Black  |   Odd   |  19-36  |
    +---------+---------+---------+---------+---------+---------+
"""


def single_number():
	number = 1.0 / 37 * (35)

	expected = -1 + number

	return expected


"""
Romanosky Bet
+---+----+----+----+----+----+----+----+----+----+----+----+----+------+
|   |  3 |  6 |  9 | 12 | 15 | 18 | 21 | 24 | 27 | 30 | 33 | 36 | 2to1 |
|   |----X----+----+----+----+----+----+----+----+----+----+----+------+
| 0 |  2 |  5 |  8 | 11 | 14 | 17 | 20 | 23 | 26 | 29 | 32 | 35 | 2to1 |
|   |----+----+----X----+----+----+----+----+----+----+----+----+------+
|   |  1 |  4 |  7 | 10 | 13 | 16 | 19 | 22 | 25 | 28 | 31 | 34 | 2to1 |
+---+----+----+----+----+----+----+----+----+----+----+----+----+------+
    |     1st Dozen     |         3X        |         3X        |
    +---------+---------+---------+---------+---------+---------+
    |   1-18  |   Even  |   Red   |  Black  |   Odd   |  19-36  |
    +---------+---------+---------+---------+---------+---------+

2 corner bets with no intersection, 2 dozen bets.
"""
def romanosky():        # win takeback
	corners	= 8.0  / 37 * (8 + 1)
	dozens	= 24.0 / 37 * (6 + 3)

	expected = -8 + corners + dozens
	# normalize
	expected = expected / 8

	return expected

"""
Modified Romanosky Bet (1)
+---+----+----+----+----+----+----+----+----+----+----+----+----+------+
|   |  3 |  6 |  9 | 12 | 15 | 18 | 21 | 24 | 27 | 30 | 33 | 36 | 2to1 |
|   |----X----+----+----+----+----+----+----+----+----+----+----+------+
| 0 |  2 |  5 |  8 | 11 | 14 | 17 | 20 | 23 | 26 | 29 | 32 | 35 | 2to1 |
|   |----+----X----+----+----+----+----+----+----+----+----+----+------+
|   |  1 |  4 |  7 | 10 | 13 | 16 | 19 | 22 | 25 | 28 | 31 | 34 | 2to1 |
+---+----+----+----+----+----+----+----+----+----+----+----+----+------+
    |     1st Dozen     |         3X        |         3X        |
    +---------+---------+---------+---------+---------+---------+
    |   1-18  |   Even  |   Red   |  Black  |   Odd   |  19-36  |
    +---------+---------+---------+---------+---------+---------+

2 corner bets with 1 intersection, 2 dozen bets.
"""
def modified_romanosky_1():# win    takeback
	star 	= 1.0  / 37 * (8 + 8 + 2)    # Number 5
	corners	= 6.0  / 37 * (8     + 1)    # Corner bets, except number 5
	dozens	= 24.0 / 37 * (6     + 3)

			  # bet
	expected = -8 + star + corners + dozens
	# normalize
	expected = expected / 8
	return expected

"""
Modified Romanosky Bet (2)
+---+----+----+----+----+----+----+----+----+----+----+----+----+------+
|   |  3 |  6 |  9 | 12 | 15 | 18 | 21 | 24 | 27 | 30 | 33 | 36 | 2to1 |
|   |----X----+----+----+----+----+----+----+----+----+----+----+------+
| 0 |  2 |  5 |  8 | 11 | 14 | 17 | 20 | 23 | 26 | 29 | 32 | 35 | 2to1 |
|   |----X----+----+----+----+----+----+----+----+----+----+----+------+
|   |  1 |  4 |  7 | 10 | 13 | 16 | 19 | 22 | 25 | 28 | 31 | 34 | 2to1 |
+---+----+----+----+----+----+----+----+----+----+----+----+----+------+
    |     1st Dozen     |         3X        |         3X        |
    +---------+---------+---------+---------+---------+---------+
    |   1-18  |   Even  |   Red   |  Black  |   Odd   |  19-36  |
    +---------+---------+---------+---------+---------+---------+

2 corner bets with 2 intersections, 2 dozen bets.
"""
def modified_romanosky_2():# win    takeback
	stars	= 2.0  / 37 * (8 + 8 + 2)    # Numbers 2, 5
	corners	= 4.0  / 37 * (8     + 1)    # Corner bets, except numbers 2, 5
	dozens	= 24.0 / 37 * (6     + 3)

			  # bet
	expected = -8 + stars + corners + dozens
	# normalize
	expected = expected / 8
	return expected

	# 				  bet (normalized) 	   average payout    normalizing bet
	#expected_payout = -1 + (1.0 * sum(payouts) / len(payouts)) / bet_sum
	# print "Expected payout: " + str(expected_payout)


def main():
	# print single_number()
	# print romanosky()
	# print modified_romanosky_1();
	# print modified_romanosky_2();

if __name__=="__main__": main()