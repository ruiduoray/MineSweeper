import Board

if __name__ == "__main__":
	"""Init the GameBoard"""
	while True:
		try:
			choice = int(input("\n\nEnter 1 to go with default setting (9 X 9 GameBoard with 10 mine)\nEnter 2 to customize\n"))

			if choice == 1:
				GameBoard = Board.Board(9,9,10)
				break
			elif choice == 2:
				while True:
					try:
						width = int(input("\nEnter GameBoard width: "))
						length = int(input("\nEnter GameBoard length: "))
						num_mine = int(input("\nEnter number of mine: "))

						GameBoard = Board.Board(length,width,num_mine)
						break
					except ValueError:
						print("Please enter a valid customization: (width > 0; length > 0 and 0 < number of mine < width * length)")
						continue
				break
			else:
				raise ValueError("Choice not 1 or 2")

		except ValueError:
			print("\nPlease enter a valid choice\n")
			continue


	while True:
		if GameBoard.Lost:
			print("You lost!")
			GameBoard.REVEALMINE()
			print(GameBoard)
			break
		if GameBoard.check_win():
			print("You won!")
			print(GameBoard)
			break
		print(GameBoard)

		try:
			choice = int(input("\n\nPlease select action to the GameBoard\nPress Control+C to quit at anytime\n1.Reveal     2.Flag/Unflag\n"))
			if choice != 1 and choice != 2:
				raise ValueError("Choice not 1 or 2")

			while True:
				try:
					r = int(input("Enter Row: ")) - 1
					c = int(input("Enter Column: ")) - 1
					if r < 0 or r >= GameBoard.length:
						raise ValueError("Invalid Row")
					if c < 0 or c >= GameBoard.width:
						raise ValueError("Invalid Column")
					break
				except ValueError:
					print("Please Enter a valid row number and a valid column number\n")
		

			if choice == 1:
				GameBoard.reveal(r,c, True)

			if choice == 2:
				GameBoard.flag(r,c)

		except ValueError:
			print("\nPlease enter a valid choice\n")


















