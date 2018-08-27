



class Game:
    '''the overall reversi game class'''

    def __init__(self):
        self.get_rules()
        self.init_players()
        self.init_board()

    @classmethod
    def start_from_config_file(cls):
        pass

    @classmethod
    def start_from_user(cls):
        pass

    def play_game(self):
        '''the overall control function for playing the game'''
        pass

    def get_rules(self):
        '''init the rules for the game'''
        pass

    def init_players(self):
        '''init the players for the game'''
        pass

    def init_board(self):
        pass

    def play_turn(self):
        pass
