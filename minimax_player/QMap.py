from board import Board
from disk import Disk
import itertools

import pickle
import numpy as np
path = 'qmap_training2.pkl'
path2 = 'qmap_training.pkl'

class QMap:

    def __init__(self, player, load=1):
        self.weights_matrix = self.weight_matrix()
        self.learning_rate = 0.2
        self.player = player
        self.enemy_color = Disk.LIGHT if player.color == Disk.DARK else Disk.DARK
        self.discount = 1

        if load:
            with open(path, 'rb') as handle:
                self.qmap = pickle.load(handle)

            #print("\nqmap - init\n",[x for x in self.qmap.items() if x[1] != 0])
        else:
            self.qmap = {}
        #product = itertools.product([Disk.NONE, Disk.LIGHT, Disk.DARK], repeat=64)


    def weight_matrix(self):
        matrix = np.array([100, -20, 10, 5, 5, 10, -20, 100,
                          -20, -50, -2,-2,-2,-2,-50,-20,
                          10,-2,-1,-1,-1,-1,-2,10,
                          5,-2,-1,-1,-1,-1,-2,5,
                          5, -2, -1, -1, -1, -1, -2, 5,
                          10, -2, -1, -1, -1, -1, -2, 10,
                          -20, -50, -2, -2, -2, -2, -50, -20,
                          100, -20, 10, 5, 5, 10, -20, 100])
        return matrix


    def update(self, action, reward, new_board, board):
        my_state, enemy_state = self.from_board_to_states(board)
        key = ((my_state, enemy_state), tuple(action))
        if key not in self.qmap:
            self.qmap[key] = 0
        self.qmap[key] = (1 - self.learning_rate) * self.qmap[key] + self.learning_rate *\
                         (reward + self.discount * self.max_q(new_board))
        self.save()

    def from_board_to_states(self, board):
        my_grade = np.array([1 if s == self.player.color else 0 for x in board.get_square_matrix() for s in x])
        my_state = my_grade.dot(self.weights_matrix)
        enemy_grade = np.array([1 if s == self.enemy_color else 0 for x in board.get_square_matrix() for s in x])
        enemy_state = enemy_grade.dot(self.weights_matrix)
        return my_state, enemy_state

    def max_q(self, new_board):
        my_state, enemy_state = self.from_board_to_states(new_board)
        new_state = (my_state, enemy_state)
        options = [[q, key] for key, q in self.qmap.items() if new_state in key]
        for move in new_board.get_possible_moves(self.player):
            if tuple(move) not in [elem[1][1] for elem in options]:
                self.qmap[(new_state, tuple(move))] = 0
                options.append([0, ((my_state, enemy_state), tuple(move))])
        val = sorted(options, key=lambda x: x[0], reverse=True)[0][0]
        return val

    def save(self, path = path):
        output = open(path, 'wb')
        pickle.dump(self.qmap, output)
        output.close()
        output = open(path2, 'wb')
        pickle.dump(self.qmap, output)
        output.close()

    def load(self, path = path):
        self.qmap = pickle.load(open(path, "rb"))

    def get_max_q(self, new_board, possible_moves):
        my_state, enemy_state = self.from_board_to_states(new_board)
        new_state = (my_state, enemy_state)
        options = [[q, key] for key, q in self.qmap.items() if new_state in key]
        poss_moves = []
        for move in possible_moves:
            if tuple(move) not in [elem[1][1] for elem in options]:
                self.qmap[(new_state, tuple(move))] = 0
                poss_moves.append([0, ((my_state, enemy_state), tuple(move))])
            else:
                poss_moves.append([options[i] for i in range(len(options)) if tuple(move) in options[i][1]][0])
        chosen = sorted(poss_moves, key=lambda x: x[0], reverse=True)[0][1][1]
        return list(chosen)
