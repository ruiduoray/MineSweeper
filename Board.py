from random import randint

class Board():
	def __init__(self, length, width, num_mine):
		if length <= 0 or width <= 0 or num_mine <= 0:
			raise ValueError("length and width and number of mines all have to be at least 1")
		if num_mine > length * width:
			raise ValueError("There will be more mines than the number of cells")


		self.length = length
		self.width = width
		self.num_mine = num_mine
		self.num_safe_cell = self.length * self.width - self.num_mine
		self.num_cell_revealed = 0


		self.count_dict = {}
		self.revealed_board = [[''] * width for _ in range(length)]
		self.mine_set = set()
		self.flag_set = set()
		self.Lost = False

		while len(self.mine_set) < self.num_mine:
			mine = randint(0, length * width - 1)
			if mine in self.mine_set:
				continue
			for i in self.get_around_nums(mine):
				self.count_dict[i] = self.count_dict.get(i, 0)+1
			self.mine_set.add(mine)


	def check_win(self):
		return self.num_cell_revealed == self.num_safe_cell or self.flag_set == self.mine_set

	def reveal(self, row, column, firstClick = False):
		if firstClick and self.revealed_board[row][column] == '!':
			self.flag(row, column)
		if self.revealed_board[row][column] != '':
			return
		num = self.row_column_to_num(row, column)
		
		if num in self.mine_set:
			self.revealed_board[row][column] = 'X'
			self.Lost = True
			return


		count = self.count_dict.get(num, 0)
		self.revealed_board[row][column] = count
		self.num_cell_revealed += 1
		if count == 0:
			for cell in self.get_around_nums(num):
				r, c = self.num_to_row_column(cell)
				self.reveal(r, c)

	def flag(self, row, column):
		if self.revealed_board[row][column] != '' and self.revealed_board[row][column]!= '!':
			return
		if self.revealed_board[row][column] == '!':
			self.revealed_board[row][column] = ''
			self.flag_set.discard(self.row_column_to_num(row,column))
		else:
			self.revealed_board[row][column] = '!'
			self.flag_set.add(self.row_column_to_num(row,column))




	"""Convertion between Row/Column and Num format to represent the postion of a cell"""
	def row_column_to_num(self, row, column):
		return row*self.width+column

	def num_to_row_column(self, num):
		return (num // self.width, num % self.width)

	"""Takes a position num and return a list of all the position num that are around it"""
	def get_around_nums(self, num):
		ret = set([num - self.width - 1, num - self.width, num - self.width + 1, num - 1,
			num + 1, num + self.width - 1, num + self.width, num + self.width + 1])
		row, column = self.num_to_row_column(num)
		if row == 0:
			ret.discard(num - self.width - 1)
			ret.discard(num - self.width)
			ret.discard(num - self.width + 1)
		if row == self.length - 1:
			ret.discard(num + self.width - 1)
			ret.discard(num + self.width)
			ret.discard(num + self.width + 1)
		if column == 0:
			ret.discard(num - self.width - 1)
			ret.discard(num - 1)
			ret.discard(num + self.width - 1)
		if column == self.width - 1:
			ret.discard(num - self.width + 1)
			ret.discard(num + 1)
			ret.discard(num + self.width + 1)
		return list(ret)


	def __str__(self):
		ret = "   "
		for i in range(1,self.width+1):
			if i < 10:
				ret += str(i) + '  '
			else:
				ret += str(i) + ' '
		count = 1
		for row in self.revealed_board:
			if count < 10:
				ret += '\n' + str(count) + '  '
			else:
				ret += '\n' + str(count) + ' '
			for cell in row:
				ret += (str(cell) or '-') + '  '
			count += 1
		return ret


	def REVEALMINE(self):
		for num in self.mine_set:
			r, c = self.num_to_row_column(num)
			self.reveal(r, c, True)

	def REVEALBOARD(self):
		for i in range(0, self.length * self.width):
			r, c = self.num_to_row_column(i)
			self.reveal(r, c, True)

	def FLAGTHEREST(self):
		for num in self.mine_set:
			r, c = self.num_to_row_column(num)
			if self.revealed_board[r][c] != 'X' or self.revealed_board[r][c] != '!':
				self.flag(r, c)


