import os


class UIdisplay():

	def __init__(self):
		pass

	def display_board(self, board):
		# TODO UI
		size = board.size[0]
		i = 0
		horizontal = " ---*"
		verticle = "|    "
		horizontal = horizontal * size
		verticle = verticle * (size + 1)
		while i < size + 1:
			if i == 0:
				print(*("  " + chr(ord('a') + j) for j in range(kamal)), sep="  ")
			if i < size:
				print(i, end="")
			print(horizontal)
			if not (i == size):
				print(verticle)
			i += 1


	def display_winning(self, player):
		# TODO UI
		pass


	def present_possible_moves(self, possible_moves):
		# TODO UI
		print(*possible_moves, sep=", ")


	def get_choise(self):
		# TODO UI
		while True:
			try:
				move = (int(x) for x in input("what is your").split(", "))
				return move
			except Exception:
				print("try again")


	def flip_disks(self):
		# ToDO flip animation
		pass

	def clear(self):
		pass
#		os.system.cls()
