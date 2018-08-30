from abstract_player import AbstractPlayer
import random
from copy import deepcopy

from disk import Disk


class RandomPlayer(AbstractPlayer):
    def __init__(self, color):
        super().__init__(color)

    def get_move(self, board, possible_moves):
        return self.minimax(board, possible_moves)


    def minimax(self, board, possible_moves):
        best_move = possible_moves[0]
        best_score = float('-inf')
        for move in possible_moves:
            abstract_board = deepcopy(board.performe_move(move, self, None))
            score = self.min_play(abstract_board)
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

    def min_play(self, board):
        if self.is_gameover(board):
            return self.evaluate(board)
        moves = board.get_possible_moves(self)
        best_score = float('inf')
        for move in moves:
            abstract_board = deepcopy(board.performe_move(move, self, None))
            score = self.max_play(abstract_board)
            if score < best_score:
                best_score = score
        return best_score

    def max_play(self, board):
        if self.is_gameover(board):
            return self.evaluate(board)
        moves = board.get_possible_moves(self)
        best_score = float('-inf')
        for move in moves:
            abstract_board = deepcopy(board.performe_move(move, self, None))
            score = self.min_play(abstract_board)
            if score > best_score:
                best_score = score
        return best_score

    def evaluate(self, board):
        cnt_dark = 0
        cnt_light = 0
        for x in board.get_square_matrix():
            for s in x:
                if s == Disk.DARK:
                    cnt_dark += 1
                elif s == Disk.LIGHT:
                    cnt_light += 1
        if self.color == Disk.DARK:
            return 1 if (cnt_dark - cnt_light) > 0 else -1
        else:
            return -1 if (cnt_dark - cnt_light) > 0 else 1
