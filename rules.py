from disk import Disk

class Rules:
    '''the class for the game rules'''

    def __init__(self):
        self.winning_rule = self.default_winning_rule
        self.flipping_rule = self.default_flipping_rules
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
        cnt_dark = 0
        cnt_light = 0
        for x in board.get_square_matrix():
            for s in x:
                if s == Disk.DARK:
                    cnt_dark += 1
                elif s == Disk.LIGHT:
                    cnt_light += 1
        for player in players:
            if player.color == Disk.DARK:
                dark_player = player
        if (cnt_dark - cnt_light) > 0:
            dark_player.set_reward(1)
            return Disk.DARK
        elif (cnt_dark - cnt_light) < 0:
            dark_player.set_reward(-1)
            return Disk.LIGHT
        else:
            dark_player.set_reward(0)
            return Disk.NONE



    def default_flipping_rules(self, square, color):
        if square.color == color:
            return
        for connection in square.get_neighbours():
            if square.get_neighbours()[connection] is None:
                continue
            if color is Disk.DARK:
                if square.get_neighbours()[connection][1] == square.light_dark:
                    square.concatenate_flip(color, connection, square.DARK)
            elif color is Disk.LIGHT:
                if square.get_neighbours()[connection][1] == square.dark_light:
                    square.concatenate_flip(color, connection)

        square.change_color(color)

    def default_create_starting_pattern(self, board):
        x1, x2 = board.size[0]//2, board.size[0]//2 - 1
        y1, y2 = board.size[1] // 2, board.size[1] // 2 - 1
        start = ([[x1, y2],Disk.DARK], [[x2, y1],Disk.DARK],[[x1, y1],Disk.LIGHT],[[x2, y2],Disk.LIGHT])
        board.init_starting_pattern(start)


    def default_possible_moves_rule(self, player, board):
        possible_squares = []
        for square in board.get_search_pool():
            for connection in square.get_neighbours():
                print(square.get_neighbours()[connection])
                if player.color == Disk.LIGHT:
                    if square.get_neighbours()[connection][1] == square.dark_light:
                        possible_squares.append(square)
                if player.color == Disk.DARK:
                    if square.get_neighbours()[connection][1] == square.light_dark:
                        possible_squares.append(square)
        return possible_squares

