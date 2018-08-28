from UI.ui import UIdisplay


class Turn:
    '''define one turn of one player'''

    def __init__(self, player, board, rules, log_path = None):
        self.player = player
        self.board = board
        self.log_move = log_path
        self.rules = rules

    def play_turn(self):
        '''the overall function'''
        #check winning in the game obj, not here
        #display the board
        UIdisplay.clear()
        self.board.display_board()
        # display moves to the player
        possible_moves = self.get_possible_moves()
        if len(possible_moves) > 0:
            try:
                self.player.present_possible_moves(possible_moves)
            except AttributeError:
                pass
            # get his move of choise
            while True:
                try:
                    move = self.player.get_move()
                    # get apdate to the board
                    self.board.flip_disk(move, self.rules.flipping_rule, self.player)
                    UIdisplay.flip_disks()
                    return 1
                except Exception:
                    "bad move, enter again"
        else:
            return 0


    def log_turn (self):
        pass


    def get_possible_moves(self):
        return self.rules.default_possible_moves_rule(self.player, self.board)

