from abstract_player import AbstractPlayer
from UI.ui import UIdisplay

class InteractivePlayer(AbstractPlayer):
    def __init__(self, color):
        super().__init__(color)

    def get_move(self, board, possible_moves):
        self.present_possible_moves(possible_moves)
        move = self.get_choise()
        return move


    def present_possible_moves(self, possible_moves):
        # TODO UI
        UIdisplay.present_possible_moves(possible_moves)



    def get_choise(self):
        # TODO UI
        return UIdisplay.get_choise()

