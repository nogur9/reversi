import math

from abstract_player import AbstractPlayer
import random
from copy import deepcopy

from disk import Disk


class SimplePlayer(AbstractPlayer):
    def __init__(self, color):
        super().__init__(color)

    def get_move(self, board, possible_moves):
        grading = []
        for move in possible_moves:
            board_tmp = deepcopy(board)
            board_tmp.performe_move(move, self, None)
            cnt_dark = 0
            cnt_light = 0
            for x in board_tmp.get_square_matrix():
                for s in x:
                    if s == Disk.DARK:
                        cnt_dark += 1
                    elif s == Disk.LIGHT:
                        cnt_light += 1
            win = 0
            if cnt_light + cnt_dark == board_tmp.size[0]*board_tmp.size[1]:
                win = 1
            if self.color == Disk.DARK:
                if win:
                    grade = math.inf if (cnt_dark-cnt_light) > 0 else -math.inf
                else:
                    grade = cnt_dark-cnt_light
            else:
                if win:
                    grade = math.inf if (cnt_dark-cnt_light) < 0 else -math.inf
                else:
                    grade = -cnt_dark+cnt_light
            grading.append(grade)

        return possible_moves[grading.index(max(grading))]
