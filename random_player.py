from abstract_player import AbstractPlayer
import random

from disk import Disk
from minimax_player.QMap import QMap

class RandomPlayer(AbstractPlayer):
    def __init__(self, color):
        super().__init__(color)
        self.reward = 0
        self.last_key = None
        self.qmap = QMap(self)
    def get_move(self, board, possible_moves):
        index = random.randint(0, len(possible_moves) - 1)
        self.get_state_action(board, possible_moves[index])
        return possible_moves[index]

    def set_reward(self, reward):
        self.reward = reward

    def update_map(self, new_board):
        new_state = "".join([str(sqr.color.value) for x in new_board.get_square_matrix() for sqr in x])
        self.qmap.update(self.key, self.reward, new_state)

    def get_state_action(self, board, move):
        key = (str(move[0]) + str(move[1]), "".join([str(sqr.color.value) for x in board.get_square_matrix() for sqr in x]))
        self.last_key = key
RandomPlayer(Disk.DARK)