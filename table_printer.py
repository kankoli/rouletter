import lib.utils as utils

class Table:
	def __init__(self):
		self.__init_table()
		self.payouts = [0] * 37
		self.bet_sum = 0
		self.bet_hsh = {}

	def __init_table(self):
		self.table = [
"+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+---------+",
"|       |       |       |       |       |       |       |       |       |       |       |       |       |         |",
"|       |   3   |   6   |   9   |   12  |   15  |   18  |   21  |   24  |   27  |   30  |   33  |   36  |   2-1   |",
"|       |       |       |       |       |       |       |       |       |       |       |       |       |         |",
"|       |-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+---------+",
"|       |       |       |       |       |       |       |       |       |       |       |       |       |         |",
"|   0   |   2   |   5   |   8   |   11  |   14  |   17  |   20  |   23  |   26  |   29  |   32  |   35  |   2-1   |",
"|       |       |       |       |       |       |       |       |       |       |       |       |       |         |",
"|       |-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+---------+",
"|       |       |       |       |       |       |       |       |       |       |       |       |       |         |",
"|       |   1   |   4   |   7   |   10  |   13  |   16  |   19  |   22  |   25  |   28  |   31  |   34  |   2-1   |",
"|       |       |       |       |       |       |       |       |       |       |       |       |       |         |",
"+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+---------+",
"        |                               |                               |                               |",
"        |             1st12             |             2nd12             |             3rd12             |",
"        |                               |                               |                               |",
"        +---------------+---------------+---------------+---------------+---------------+---------------+",
"        |               |               |               |               |               |               |",
"        |      1-18     |     Even      |      Red      |     Black     |      Odd      |     19-36     |",
"        |               |               |               |               |               |               |",
"        +---------------+---------------+---------------+---------------+---------------+---------------+"]

	def bet_prompt(self, prompt):
		command, bet = prompt.split(":")
		code = command[0]
		code_numbers = command[1:].split("-") if command[1:] != "" else []

		self.__place_bet(code, code_numbers, bet)
		self.__process_bet_hsh()

	def __place_bet(self, code, code_numbers, bet):
		print "__place_bet", utils.get_bet_numbers(code, code_numbers)
		bet_numbers, bet_info = utils.get_bet_numbers(code, code_numbers)
		self.payouts = utils.add_payouts(code, self.payouts, bet_numbers, bet)
		self.bet_hsh = utils.add_bet_hsh(code, bet, bet_info, self.bet_hsh)
		self.bet_sum += int(bet)

	def __process_bet_hsh(self):
		self.__init_table()
		for func in self.bet_hsh:
			for value in self.bet_hsh[func]:
				eval("self." + func)(*value)

	streets = [[10+8*i,11] for i in range(12)] + [5]
	def street(self, bet, index):
		self.__bet(bet, Table.streets, index)

	lines = [[14+8*i,11] for i in range(11)] + [5]
	def six_line(self, bet, index):
		self.__bet(bet, Table.lines, index)

	def dozen(self, bet, index):
		self.__bet(bet, [[22,13],[54,13],[86,13],5], index)

	def half(self, bet, index):
		self.__bet(bet, [[14,17],[94,17],5], index)

	def even(self, bet):
		self.__bet(bet, [[30,17],5], 0)
	def odd(self, bet):
		self.__bet(bet, [[78,17],5], 0)

	def red(self, bet):
		self.__bet(bet, [[46,17],5], 0)
	def black(self, bet):
		self.__bet(bet, [[62,17],5], 0)

	def avenue(self, bet, index):
		self.__bet(bet, [[107,9],[107,5],[107,1],5], index)

	straights = [[10+8*i,j] for i in range(36) for j in [1,5,9]]
	straights = [[2,5]] + straights + [5]
	def straight(self, bet, index):
		self.__bet(bet, Table.straights, index)

	edges = [
	[[14+8*i,j] for i in range(11) for j in [1,5,9]],
	[[10+8*i,j] for i in range(12) for j in [3,7]],
	[[14+8*i,j] for i in range(11) for j in [3,7]],
	5
	]
	def edge(self, bet, index, type):
		self.__bet(bet, Table.edges[type] + [Table.edges[-1]], index)

	def square(self, bet, index):
		self.__bet(bet, Table.edges[2] + [Table.edges[-1]], index)


	def __bet(self, bet, places, index):
		bet = str(bet)
		table = self.table

		offsetx = places[index][0]
		offsety = places[index][1]
		width = places[-1]
		output = [("*"*len(bet)).center(width), "*" + (bet).center(width-2) + "*", ("*"*len(bet)).center(width)]
		for i, row in enumerate(output):
			table[offsety + i] = table[offsety + i][:offsetx] + row + table[offsety + i][offsetx + len(row):]

	def __str__(self):
		return reduce(lambda x, y: x + "\n" + y, self.table, "")
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

	def do_tests(self):
		self.test2()
		print self
		self.test1()
		print self
		self.test3()
		print self
		self.test4()
		print self

def main():
	tp = Table()
	tp.do_tests()

if __name__=="__main__":main()