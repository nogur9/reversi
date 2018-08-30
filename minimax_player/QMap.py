from board import Board
from disk import Disk
import itertools
import pickle
import numpy as np
path = 'qmap.pkl'
class QMap:

    def __init__(self, player, load=0):
        self.learning_rate = 0.3
        product = itertools.product([Disk.NONE, Disk.LIGHT, Disk.DARK], repeat=64)
        self.discount = 0.8
        if load:
            with open('qmap.pkl', 'rb') as handle:
                self.qmap = pickle.load(handle)
        else:
            self.qmap = {}
            for iter in product:
                board = Board(8)
                for x in range(8):
                    for y in range(8):
                        board.square_matrix[x][y] = iter[8*x+y]
                for move in board.get_possible_moves(player):
                #key is action, state -  num_x, num_y, 64 colors of the board
                    key = (str(move[0])+str(move[1]), "".join([str(sqr.value) for sqr in iter]))
                    self.qmap[key] = 0
            self.save()

    def weight_matrix(self):
        matrix = np.array([100, -20, 10, 5, 5, 10, -20, 100,
                          -20, -50, -2,-2,-2,-2,-50,-20,
                          10,-2,-1,-1,-1,-1,-2,10,
                          5,-2,-1,-1,-1,-1,-2,5,
                          5, -2, -1, -1, -1, -1, -2, 5,
                          10, -2, -1, -1, -1, -1, -2, 10,
                          -20, -50, -2, -2, -2, -2, -50, -20,
                          100, -20, 10, 5, 5, 10, -20, 100])


    def update(self, key, reward, new_state):
        if ((my_state, enemy_state), action) not in self.qmap:
            self.qmap[((my_state, enemy_state), action)] = 0
        self.qmap[key] = (1 - self.learning_rate) * self.qmap[key] + self.learning_rate *\
                         (reward + self.discount * self.max_q(new_state))

    def from_board_to_states(self, board):
        my_grade = np.array([1 if s == self.player.color else 0 for x in board.get_square_matrix() for s in x])
        my_state = my_grade.dot(self.weights_matrix)
        enemy_grade = np.array([1 if s == self.enemy.color else 0 for x in board.get_square_matrix() for s in x])
        enemy_state = enemy_grade.dot(self.weights_matrix)
        return my_state, enemy_state

    def max_q(self, new_state, board):
        options = [q for key, q in self.qmap.items() if new_state in key]
        for move in board.get_possible_moves(self.player):
            if move not in options
            key = (str(move[0]) + str(move[1]), "".join([str(sqr.value) for sqr in iter]))
            self.qmap[key] = 0
        val = max([q for key, q in self.qmap.items() if new_state in key])
        return val

    def save(self, path = path):
        output = open(path, 'wb')
        pickle.dump(self.qmap, output)
        output.close()

    def load(self, path = path):
        output = open(path, 'wb')
        pickle.dump(self.qmap, output)
        output.close()