from abstract_player import AbstractPlayer
import random
from minimax_player.QMap import QMap

class QPlayer(AbstractPlayer):
    def __init__(self, color, time_per_turn = 5):
        super().__init__(color, time_per_turn)
        self.reward = 0
        self.last_key = None
        self.qmap = QMap(self)

    def get_move(self, board, possible_moves):
        move = self.qmap.get_max_q(board, possible_moves)
        self.get_state_action(board, move)
        return move

    def set_reward(self, reward):
        self.reward = reward

    def update_map(self, new_board):
        former_board, move = self.last_key
        self.qmap.update(move, self.reward, new_board, former_board)

    def get_state_action(self, board, move):
        self.last_key = (board, move)
