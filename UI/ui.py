import os

from game import Game

class UIdisplay(Game):

	def __init__(self):
		pass

	def display_board(self, board):
		# TODO UI
		pass


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
		os.system.cls()
