
class Turn:
    '''define one turn of one player'''

    def __init__(self):
        self.player = None
        self.board = None
        self.log_move = None
        self.possible_moves_rules =None
        self.flipping_disks_rules = None
        self.players_move = None


    def play_turn(self):
        '''the overall function'''
        pass


    def get_possible_moves(self):
        '''calc the possible moves of the turn by the possible moves of the player'''
        pass


    def present_possible_moves(self):
        '''the ui shit'''
        pass


    def get_players_move(self):
        '''get the player's respond'''
        pass


    def calc_flipped_disks(self):
        pass


    def flip_disks(self):
        '''ui shit'''
        pass


    def log_turn (self):
        pass