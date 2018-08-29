from board import Board
from disk import Disk
import itertools
from abstract_player import AbstractPlayer
class QMap:
    alpha = 1
    gamma = 0.8
    def __init__(self):
        product = itertools.product([Disk.NONE, Disk.LIGHT, Disk.DARK], repeat=64)
        self.qmap = {}
        players = [AbstractPlayer(Disk.LIGHT), AbstractPlayer(Disk.DARK)]
        for player in players:
            for iter in product:
                board = Board(8)
                for x in range(8):
                    for y in range(8):
                        board[x][y] = iter[8*x+y]
                for move in board.get_possible_moves(player):
                #key is player_color, num_x, num_y, 64 colors of the board
                    key = str(player.color.value)+str(x)+str(y)+"".join([str(sqr.color.value) for sqr in iter])
                    self.qmap[key] = 1
    def update (self, key, reward):
        self.qmap[key] =

class VMap:

    def __init__(self):
        product = itertools.product([Disk.NONE, Disk.LIGHT, Disk.DARK], repeat=64)
        vmap = {board: 1 for board in product}
