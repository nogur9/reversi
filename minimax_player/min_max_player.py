from abstract_player import AbstractPlayer
import random
from copy import deepcopy
max_depth = 1
from disk import Disk


class MinimaxPlayer(AbstractPlayer):
    def __init__(self, color):
        super().__init__(color)

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


    def set_reward(self, o):
        pass


    def update_map(self, c):
        pass