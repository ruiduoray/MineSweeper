"""
GUI.py
A very simple GUI of minsweeper. Graphics by Yujie Qiu, yujieqiu55@gmail.com
Support MAC OS (Windows OS should work as well but need to change the button event name)
Run with the command"python3 GUI.py" in terminal
ruiduoray@berkeley.edu 2/13/2020

"""

from Board import *
from tkinter import *
from functools import partial


class Game:
	def __init__(self, root):
		self.root = root
		self.new_game()
		

	def new_game(self):
		def choice1func():
			frame.destroy()
			self.play_game(Board(9, 9, 10))

		def choice2func():
			frame.destroy()
			self.customize()

		frame = Frame(self.root)
		frame.pack()
		Label(frame, text = "Welcome to MineSweeper").grid(row = 0)
		Button(frame, width = 15,  text = "Default Setting", command = choice1func).grid(row = 1)
		Button(frame,  width = 15,text = "Customize Setting", command = choice2func).grid(row = 2)


	def customize(self):
		def Generate():
			try:
				width = int(widthEntry.get())
				length = int(lengthEntry.get())
				num_mine = int(num_mineEntry.get())

				widthEntry.delete(0, END)
				lengthEntry.delete(0, END)
				num_mineEntry.delete(0, END)
			except ValueError:
				Message(frame, text = "Please enter a valid customization: (width > 2; length > 2 and 0 < number of mine < width * length)").grid(row = 5, columnspan=2)
				return
			try:	
				board = Board(width, length, num_mine)
			except ValueError as e:
				Message(frame, text = e.args[0]).grid(row = 5, columnspan = 2)
				return
			frame.destroy()
			self.play_game(board)

			

		frame = Frame(self.root)
		frame.pack()
		Label(frame, text = "Customizing").grid(row = 0, columnspan = 2)
		Label(frame, text = "width:").grid(row = 1, column = 0, sticky = E)
		Label(frame, text = "length:").grid(row = 2, column = 0, sticky = E)
		Label(frame, text = "count of mine:").grid(row = 3, column = 0, sticky = E)
		widthEntry = Entry(frame, width = 5)
		widthEntry.grid(row = 1, column = 1)
		lengthEntry = Entry(frame, width = 5)
		lengthEntry.grid(row = 2, column = 1)
		num_mineEntry = Entry(frame, width = 5)
		num_mineEntry.grid(row = 3, column = 1)
		Button(frame, text = "Generate!", command = Generate).grid(row = 4, column = 1)




	def play_game(self, board):
		ENDGAME = False
		def end_game(msg):
			nonlocal ENDGAME
			ENDGAME = True
			Label(frame, text = msg).grid(row = board.length + 1, columnspan = board.width)
			Button(frame, text = "New Game", command = restart).grid(row = board.length + 2, column = 0, columnspan = 3)
			Button(frame, text = "Quit", command = quit_game).grid(row = board.length + 2, column = 3, columnspan = 2)

		def restart():
			frame.destroy()
			self.new_game()

		def quit_game():
			frame.destroy()
			self.root.destroy()

		ori_reveal = board.reveal
		ori_flag = board.flag

		def new_reveal(row, column, _ = None):
			if ENDGAME:
				return
			ori_reveal(row, column)
			buttons[row][column].config(image = Game.IMAGES[str(board.revealed_board[row][column])])
			if board.Lost:
				end_game("You lost!")
			if board.check_win():
				end_game("You Won!")
		def new_flag(row, column, _ = None):
			if ENDGAME:
				return
			ori_flag(row, column)
			buttons[row][column].config(image = Game.IMAGES[str(board.revealed_board[row][column])])
			mine_label.config(text = str(board.num_mine - len(board.flag_set)))
			if board.check_win():
				end_game("You Won!")

		frame = Frame(self.root)
		frame.pack()


		board.reveal = new_reveal
		board.flag = new_flag

		buttons = []
		for i in range(board.length):
			temp = []
			for j in range(board.width):
				button = Button(frame, image = Game.IMAGES[''])
				button.bind("<Button-1>", partial(board.reveal, i, j))
				button.bind("<Button-2>", partial(board.flag, i, j))
				button.row = i
				button.column = j
				button.grid(row = i, column = j)
				temp.append(button)
			buttons.append(temp)
		Label(frame, image = Game.IMAGES['X']).grid(row = board.length, column = board.width - 2)
		mine_label = Label(frame, text = str(board.num_mine - len(board.flag_set)))
		mine_label.grid(row = board.length, column = board.width - 1)


		


if __name__ == "__main__":
	root = Tk()
	root.title("MineSweeper")
	root.geometry("+600+200")


	Game.IMAGES = {
		'':PhotoImage(file = 'images/blank.png'),
		'X':PhotoImage(file = 'images/bomb.png'),
		'!':PhotoImage(file = 'images/flag.png'),
		'0':PhotoImage(file = 'images/0.png'),
		'1':PhotoImage(file = 'images/1.png'),
		'2':PhotoImage(file = 'images/2.png'),
		'3':PhotoImage(file = 'images/3.png'),
		'4':PhotoImage(file = 'images/4.png'),
		'5':PhotoImage(file = 'images/5.png'),
		'6':PhotoImage(file = 'images/6.png'),
		'7':PhotoImage(file = 'images/7.png'),
		'8':PhotoImage(file = 'images/8.png')
		}
	game = Game(root)

	root.mainloop()


