from UI.ui import UIdisplay


class Turn:
    '''define one turn of one player'''

    def __init__(self, player, board, rules, ui, log_path = None):
        self.player = player
        self.board = board
        self.log_move = log_path
        self.rules = rules
        self.ui = ui
    def play_turn(self):
        '''the overall function'''

        self.ui.clear()
        self.board.display_board()
        # display moves to the player
        possible_moves = self.get_possible_moves()
        if len(possible_moves) > 0:
            # get his move of choise
            while True:
                try:
                    move = self.player.get_move()
                    # get apdate to the board
                    self.board.flip_disk(move, self.rules.flipping_rule, self.player)
                    UIdisplay.flip_disks()
                    return 1
                except Exception as exc:
                    print("bad move, enter again", exc)
        else:
            return 0


    def log_turn (self):
        pass


    def get_possible_moves(self):
        return self.rules.default_possible_moves_rule(self.player, self.board)

