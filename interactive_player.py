from abstract_player import AbstractPlayer
from UI.ui import UIdisplay

class InteractivePlayer(AbstractPlayer):
    def __init__(self, color):
        super().__init__(color)

    def get_move(self, board, possible_moves):
        ui = UIdisplay()
        self.present_possible_moves(possible_moves, ui)
        move = self.get_choise(ui)
        return move


    def present_possible_moves(self, possible_moves,ui):
        # TODO UI
        ui.present_possible_moves(possible_moves)



    def get_choise(self,ui):
        # TODO UI
        return ui.get_choise()

