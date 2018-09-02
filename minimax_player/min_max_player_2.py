import numpy as np

from abstract_player import AbstractPlayer
import random
from copy import deepcopy

max_depth = 1
from disk import Disk


class MinimaxPlayer2(AbstractPlayer):
    def __init__(self, color):
        super().__init__(color)
        self.weights_matrix = self.weight_matrix()

    def get_move(self, board, possible_moves):
        move = self.minimax(board, possible_moves, 0)
        return move


    def minimax(self, board, possible_moves, depth):
        if depth == max_depth:
            return self.evaluate(board)
        if len(possible_moves) == 0:
            return None
        best_move = possible_moves[0]
        best_score = float('-inf')
        for move in possible_moves:
            abstract_board = deepcopy(board)
            abstract_board.performe_move(move, self, None)
            score = self.min_play(abstract_board, depth)
            if score > best_score:
                best_move = move
                best_score = score
        return best_move

    def is_gameover (self, board):
        for x in board.get_square_matrix():
            for s in x:
                if s == Disk.NONE:
                    return 0
                else:
                    return 1

    def min_play(self, board, depth):
        if depth == max_depth:
            return self.evaluate(board)
        if self.is_gameover(board):
            return self.evaluate(board)
        moves = board.get_possible_moves(self)
        best_score = float('inf')
        for move in moves:
            abstract_board = deepcopy(board)
            abstract_board.performe_move(move, self, None)
            score = self.max_play(abstract_board, depth+1)
            if score < best_score:
                best_score = score
        return best_score

    def max_play(self, board, depth):
        if depth == max_depth:
            return self.evaluate(board)
        if self.is_gameover(board):
            return self.evaluate(board)
        moves = board.get_possible_moves(self)
        best_score = float('-inf')
        for move in moves:
            abstract_board = deepcopy(board)
            abstract_board.performe_move(move, self, None)
            score = self.min_play(abstract_board, depth+1)
            if score > best_score:
                best_score = score
        return best_score

    def evaluate(self, board):
        return self.from_board_to_states(board)


    def set_reward(self, o):
        pass

    def update_map(self, c):
        pass

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

    def from_board_to_states(self, board):
        my_grade = np.array([1 if s == self.color else 0 for x in board.get_square_matrix() for s in x])
        my_state = my_grade.dot(self.weights_matrix)
        return my_state
