from disk import Disk
"""thinkkkkkkkkkkkkkkkkkkkkkkkk"""

class Rules:
    '''the class for the game rules'''

    def __init__(self):
        self.winning_rules = self.default_winning_rule
        self.flipping_rules = self.default_flipping_rules
        self.starting_pattern = self.default_create_starting_pattern
        self.possible_moves_rule = self.default_possible_moves_rule

        #ignoring for now :(
        self.board_shape = None
        self.num_of_players = 2

    def set_winning_rules(self, rule):
        self.winning_rules = rule


    def set_flipping_rules(self, rule):
        self.flipping_rules = rule


    def set_starting_pattern(self, rule):
        self.starting_pattern = rule


    def set_possible_moves_rule(self, rule):
        self.possible_moves_rule = rule


    def set_board_shape(self, shape):
        self.board_shape = shape


    def set_num_of_players(self, num_of_players):
        self.num_of_players = num_of_players


    def default_winning_rule(self, board, *players):
        count_dict = {player.color: 0 for player in players}
        for x in board.get_square_matrix():
            for square in x:
                if square.color:
                    count_dict[square.color] += 1
        winning_color = max(count_dict, key=count_dict.get)
        for player in players:
            if player.color == winning_color:
                return player


    def default_flipping_rules(self, square, color):
        if square.color == color:
            return
        for connection in square.neighbours:
            if color is Disk.DARK:
                if connection[1] == square.light_dark:
                    square.concatenate_flip(color, connection, square.DARK)
            elif color is Disk.LIGHT:
                if connection[1] == square.dark_light:
                    square.concatenate_flip(color, connection)

        square.change_color()

    def default_create_starting_pattern(self, board):
        x1, x2 = board.size[0]//2, board.size[0]//2 + 1
        y1, y2 = board.size[1] // 2, board.size[1] // 2 + 1
        board.get_square_matrix()[x1][y2].change_color(Disk.DARK)
        board.get_square_matrix()[x2][y1].change_color(Disk.DARK)
        board.get_square_matrix()[x1][y1].change_color(Disk.LIGHT)
        board.get_square_matrix()[x2][y2].change_color(Disk.LIGHT)


    def default_possible_moves_rule(self, player, board):
        possible_squares = []
        for square in board.get_search_pool():
            for connection in square.neighbours:
                if player.color == Disk.LIGHT:
                    if connection[1] == square.dark_light:
                        possible_squares.append(square)
                if player.color == Disk.DARK:
                    if connection[1] == square.light_dark:
                        possible_squares.append(square)


