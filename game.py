from rules import Rules
from random_player import RandomPlayer
from interactive_player import InteractivePlayer
from computer_player import ComputerPlayer
from disk import Disk
from board import Board
from UI.ui import UIdisplay
from turn import Turn


class Game:
    '''the overall reversi game class'''
    human_player_class = InteractivePlayer
    computer_player1_class = RandomPlayer
    computer_player2_class = RandomPlayer


    def __init__(self, num_of_human_players = 0 , board_size=8, board_y_axis_size=0):
        self.get_rules()
        self.init_players(num_of_human_players)
        self.init_board(board_size, board_y_axis_size)
        self.init_ui()


    def play_game(self):
        '''the overall control function for playing the game'''

        # 0. create counter for the turns

        turns_iterator = self.turns_iter()

        # 0.5 . handle time
        while True:
            player = next(turns_iterator)
            # stop if - no moves left
            for key in self.moves_left:
                if self.moves_left[key]:
                    break
            else:
                self.check_winner()
                break
            if self.moves_left[player.color]:
                self.play_turn(player)


    @classmethod
    def start_from_config_file(cls):
        pass


    @classmethod
    def start_from_user(cls):
        pass


    @classmethod
    def default_start(cls):
        num_of_human_players = 2
        return cls(num_of_human_players=num_of_human_players, board_size=4)

    def get_rules(self):
        '''init the rules for the game'''
        self.rules = Rules()

    def init_players(self, num_of_human_players):
        '''init the players for the game'''
        if num_of_human_players > 2 or num_of_human_players < 0:
            raise ValueError
        self.players = []
        player1_color = Disk.LIGHT
        player2_color = Disk.DARK
        self.moves_left = {player1_color: 1,player2_color: 1}
        for i in range(num_of_human_players):
            if i:
                self.players.append(self.human_player_class(player2_color))
            else:
                self.players.append(self.human_player_class(player1_color))
        for i in range(2 - num_of_human_players):
            if i:
                self.players.append(self.computer_player1_class(player1_color))
            else:
                self.players.append(self.computer_player2_class(player2_color))


    def init_board(self, board_size, board_y_axis_size = 0):
        self.board = Board(board_size, ysize=board_y_axis_size)
        self.rules.starting_pattern(self.board, self.players[0], self.players[1])

    def init_ui(self):
        self.ui = UIdisplay()

    def play_turn(self, player):
        new_turn = Turn(player, self.board, self.rules, self.ui)
        result = new_turn.play_turn()
        self.moves_left[player.color] = result


    def check_winner(self):
        winner = self.rules.winning_rule(self.board, *(self.players))
        self.ui.display_winning(winner)

    def turns_iter(self):
        while True:
            for player in self.players:
                yield player

    def create_timer(self, player):
        pass