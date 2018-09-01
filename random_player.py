from abstract_player import AbstractPlayer
import random
from minimax_player.QMap import QMap

class RandomPlayer(AbstractPlayer):
    def __init__(self, color):
        super().__init__(color)
        self.reward = 0
        self.last_key = None
        self.qmap = QMap(self)

    def get_move(self, board, possible_moves):
        #print("random get move")
        index = random.randint(0, len(possible_moves) - 1)
        self.get_state_action(board, possible_moves[index])
        return possible_moves[index]

    def set_reward(self, reward):
        self.reward = reward

    def update_map(self, new_board):
        former_board, move = self.last_key
        self.qmap.update(move, self.reward, new_board, former_board)

    def get_state_action(self, board, move):
        self.last_key = (board, move)

