import lib.utils as utils

code_hsh = {
	"N": "straight",
	"C": "square",
	"E": "edge",
	"S": "street",
	"L": "six_line",
	"D": "dozen",
	"A": "avenue",
	"H": "half",
	"V": "even",
	"O": "odd",
	"R": "red",
	"B": "black"
}

class Table:
	def __init__(self):
		self.payouts = [0] * 37
		self.bet_sum = 0
		self.bet_hsh = {}
		self.table_drawer = utils.TableDrawer()
	
	def bet_prompt(self, prompt):
		command, bet = prompt.split(":")
		bet_type = command[0]
		bet_numbers = command[1:].split("-") if command[1:] != "" else []

		self.__place_bet(bet_type, bet_numbers, bet)

	def __place_bet(self, bet_type, bet_numbers, bet):
		bet_numbers, bet_info = self.get_bet_numbers(bet_type, bet_numbers)
		self.add_payouts(bet_type, bet_numbers, bet)
		self.add_bet_hsh(bet_type, bet, bet_info)
		self.bet_sum += int(bet)
		
	def get_bet_numbers(self, bet_type, args):
		if bet_type in code_hsh:
			return eval("utils.get_" + code_hsh[bet_type])(*args)
		else:
			raise Exception("[Get Numbers] Unknown bet type: " + str(bet_type))

	def add_bet_hsh(self, bet_type, bet, bet_info, undo=False):
		if bet_type in code_hsh:
			key = code_hsh[bet_type]
			value = [[bet]+bet_info]
			if key in self.bet_hsh:
				self.bet_hsh[key] += value
			else:
				self.bet_hsh[key] = value
		else:
			raise Exception("[Payouts] Unknown bet type: " + str(bet_type))

	def add_payouts(self, bet_type, bet_numbers, bet, undo=False):
		if bet_type in code_hsh:
			args = [self.payouts, bet_numbers, bet, undo]
			return eval("utils.payout_" + code_hsh[bet_type])(*args)
		else:
			raise Exception("[Payouts] Unknown bet type: " + str(bet_type))

	def print_payout_stats(self):
		s = ""
		s += "Total bet:" + str(self.bet_sum) + "\n"
		s += "Payouts on numbers:" + str(self.payouts) + "\n"
		payout_hsh = {}
		for payout in self.payouts:
			if payout in payout_hsh:
				payout_hsh[payout] += 1
			else:
				payout_hsh[payout] = 1

		for key in sorted(payout_hsh.keys()):
			s += str(key - self.bet_sum).rjust(3) + " | %" + str(100.0 * payout_hsh[key] / 37) + "\n"

		print s

	def __str__(self):
		self.table_drawer.process_bet_hsh(self.bet_hsh)
		return str(self.table_drawer)
	__repr__=__str__

	def test1(self):
		self.avenue(1, 0)
		self.avenue(2, 1)
		self.avenue(3, 2)

		self.dozen(1, 0)
		self.dozen(1, 1)
		self.dozen(2, 2)

		self.half(6, 0)
		self.half(9, 1)

		self.even(1)
		self.odd(2)

		self.red(2)
		self.black(4)
		
		for i in range(37):
			self.straight(1, i)

		for i in range(len(Table.edges[0])):
			self.edge(2, i, 0)
		for i in range(len(Table.edges[1])):
			self.edge(3, i, 1)
		for i in range(len(Table.edges[2])):
			self.square(4, i)

		for i in range(12):
			self.street(5, i)

		for i in range(11):
			self.six_line(6, i)

	def test2(self):
		self.avenue(2, 1)
		self.dozen(2, 2)
		self.even(1)
		self.black(4)
		self.half(6, 0)
		
		self.straight(1, 10)
		self.edge(2, 17, 0)
		self.edge(2, 7, 1)
		self.square(4, 15)
		self.street(5, 9)
		self.six_line(6, 6)

	def test3(self):
		bet_hsh = {}
		bet_hsh["street"] = [[2, 5]]
		bet_hsh["avenue"] = [[3, 2]]
		bet_hsh["dozen"] = [[1, 1]]
		bet_hsh["even"] = [[4]]
		bet_hsh["black"] = [[9]]
		bet_hsh["half"] = [[5,1]]
		bet_hsh["straight"] = [[8,14]]
		bet_hsh["edge"] = [[1,14,0]]
		bet_hsh["corner"] = [[2,5]]
		bet_hsh["line"] = [[3,8]]
		self.__process_bet_hsh(bet_hsh)

	def test4(self):
		self.bet_prompt("N10:1")
		self.bet_prompt("N0:1")
		self.bet_prompt("C1-5:2")
		self.bet_prompt("C6-8:3")
		self.bet_prompt("E11-12:4")
		self.bet_prompt("E15-18:5")
		self.bet_prompt("D2:1")
		self.bet_prompt("A0:2")
		self.bet_prompt("S4:1")
		self.bet_prompt("L4-7:2")
		self.bet_prompt("V:4")
		self.bet_prompt("O:3")
		self.bet_prompt("R:2")
		self.bet_prompt("B:1")
		self.bet_prompt("H1:1")
		self.bet_prompt("H0:1")

	def test_squares(self):
		map(lambda x: self.bet_prompt("C"+str(x)+"-"+str(x+4)+":"+str(x)), [3*(x/2) + (x)%2 + 1 for x in range(22)])

	def test_edges(self):
		map(lambda x: self.bet_prompt("E"+str(x)+"-"+str(x+3)+":"+str(x)), [x+1 for x in range(33)])
		map(lambda x: self.bet_prompt("E"+str(x)+"-"+str(x+1)+":"+str(x)), [x+1 for x in range(35) if (x+1)%3 != 0])

	def do_tests(self):
		# self.test2()
		# print self
		# self.test1()
		# print self
		# # self.test3()
		# # print self
		self.test_edges()
		print self


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
def romanosky(tp):        # win takeback
	tp.bet_prompt("C2-6:1")
	tp.bet_prompt("C7-11:1")
	tp.bet_prompt("D1:3")
	tp.bet_prompt("D2:3")
	print tp

def main():
	tp = Table()
	romanosky(tp)

if __name__=="__main__":main()