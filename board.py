from disk import Disk
from copy import deepcopy

class Board:
    '''the game board'''
    def __init__(self, size, ysize=0):
        if ysize:
            self.size = (size, ysize)
        else:
            self.size = (size, size)
        self.square_matrix = []
        for x in range(self.size[0]):
            self.square_matrix.append([])
            for y in range(self.size[1]):
                self.square_matrix[x].append(Disk.NONE)

    def init_starting_pattern(self, pattern):
        for s in pattern:
            self.square_matrix[s[0][0]][s[0][1]] = s[1]

    def get_square_matrix(self):
        return self.square_matrix


    def is_valid(self, player, move):

        if self.square_matrix[move[0]][move[1]] != Disk.NONE:
            return False

        else:
            neighbours = []
            for i in range(max(0, move[0] - 1), min(move[0] + 2, self.size[0])):
                for j in range(max(0, move[1] - 1), min(move[1] + 2, self.size[1])):
                    if self.square_matrix[i][j] != None:
                        neighbours.append([i, j])
            neighbours.remove(move)
            if not len(neighbours):
                return False
            else:
                valid = False
                for neighbour in neighbours:
                    n_x = neighbour[0]
                    n_y = neighbour[1]
                    if self.square_matrix[n_x][n_y] == player.color:
                        continue
                    else:
                        tmp_x = n_x
                        tmp_y = n_y
                        x_delta = n_x - move[0]
                        y_delta = n_y - move[1]
                        while 0 <= tmp_x < self.size[0] and 0 <= tmp_y < self.size[1]:
                            if self.square_matrix[tmp_x][tmp_y] == None or self.square_matrix[tmp_x][tmp_y] == Disk.NONE:
                                break
                            if self.square_matrix[tmp_x][tmp_y] == player.color:
                                valid = True
                                break
                            tmp_x += x_delta
                            tmp_y += y_delta
                return valid


    def performe_move(self, move, player, rule):
        if not self.is_valid(player, move):
            raise ValueError
            return
        array = deepcopy(self.square_matrix)
        colour = player.color
        array[move[0]][move[1]] = colour

        neighbours = []
        for i in range(max(0, move[0] - 1), min(move[0] + 2, self.size[0])):
            for j in range(max(0, move[1] - 1), min(move[1] + 2, self.size[1])):
                if array[i][j] != None:
                    neighbours.append([i, j])
        neighbours.remove(move)

        convert = []
        for neighbour in neighbours:
            n_x = neighbour[0]
            n_y = neighbour[1]
            if array[n_x][n_y] != colour:
                path = []
                tmp_x = n_x
                tmp_y = n_y
                x_delta = n_x - move[0]
                y_delta = n_y - move[1]
                while 0 <= tmp_x < self.size[0] and 0 <= tmp_y < self.size[1]:
                    path.append([tmp_x, tmp_y])
                    value = array[tmp_x][tmp_y]
                    if value == None or value == Disk.NONE:
                        break
                    if value == colour:
                        for node in path:
                            convert.append(node)
                        break
                    tmp_x += x_delta
                    tmp_y += y_delta

        for node in convert:
            array[node[0]][node[1]] = colour
        self.square_matrix = array

    def get_possible_moves(self,player):
        valid_moves = []
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if self.is_valid(player, [i,j]):
                    valid_moves.append([i,j])
        return valid_moves


    def score(self):
        """ returns the current score for the board as a tuple
            containing # of black pieces, # of white pieces """
        dark = light = 0
        for row in self.square_matrix:
            for square in row:
                if (square == Disk.DARK):
                    dark = dark + 1
                elif (square == Disk.LIGHT):
                    light = light + 1
        return (dark, light)
