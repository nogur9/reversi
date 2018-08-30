from board import Board
from disk import Disk
import itertools
import pickle
import shelve

class QMap:

    def __init__(self, player, load=0):
        self.learning_rate = 0.3
        product = itertools.product([Disk.NONE, Disk.LIGHT, Disk.DARK], repeat=64)
        self.discount = 0.8
        if load:
            with open('myfile.pkl', 'rb') as handle:
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


    def update(self, key, reward, new_state):
        self.qmap[key] = (1 - self.learning_rate) * self.qmap[key] + self.learning_rate *\
                         (reward + self.discount * self.max_q(new_state))


    def max_q(self, new_state):
        val = max([v for k, v in self.qmap.items() if new_state in k])
        return val

    def save(self, path = 'myfile.pkl'):
        output = open(path, 'wb')
        pickle.dump(self.qmap, output)
        output.close()

    def load(self, path = 'myfile.pkl'):
        output = open(path, 'wb')
        pickle.dump(self.qmap, output)
        output.close()