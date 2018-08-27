from abstract_player import AbstractPlayer
import random


class InteractivePlayer(AbstractPlayer):
    def __init__(self, color):
        super().__init__(color)

    def get_move(self, board, possible_moves):
        self.present_possible_moves()
        move = self.get_choise()
        return move


    def present_possible_moves(self, possible_moves):
        pass


    def get_choise(self):
        while True:
            try:
                move = (int(x) for x in input("what is your").split(", "))
                return move
            except Exception:
                print("try again")
