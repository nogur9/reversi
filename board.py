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

        # If there's already a piece there, it's an invalid move
        if self.square_matrix[move[0]][move[1]] != Disk.NONE:
            return False

        else:
            # Generating the list of neighbours
            neighbours = []
            for i in range(max(0, move[0] - 1), min(move[0] + 2, self.size[0])):
                for j in range(max(0, move[1] - 1), min(move[1] + 2, self.size[1])):
                    if self.square_matrix[i][j] != None:
                        neighbours.append([i, j])
            # If there's no neighbours, it's an invalid move
            neighbours.remove(move)
            if not len(neighbours):
                return False
            else:
                # Iterating through neighbours to determine if at least one line is formed
                valid = False
                for neighbour in neighbours:

                    neighX = neighbour[0]
                    neighY = neighbour[1]

                    # If the neighbour colour is equal to your colour, it doesn't form a line
                    # Go onto the next neighbour
                    if self.square_matrix[neighX][neighY] == player.color:
                        continue
                    else:
                        # Determine the direction of the line
                        deltaX = neighX - move[0]
                        deltaY = neighY - move[1]
                        tempX = neighX
                        tempY = neighY

                        while 0 <= tempX < self.size[0] and 0 <= tempY < self.size[1]:
                            # If an empty space, no line is formed
                            if self.square_matrix[tempX][tempY] == None:
                                break
                            # If it reaches a piece of the player's colour, it forms a line
                            if self.square_matrix[tempX][tempY] == player.color:
                                valid = True
                                break
                            # Move the index according to the direction of the line
                            tempX += deltaX
                            tempY += deltaY
                return valid


    # FUNCTION: Returns a board after making a move according to Othello rules
    # Assumes the move is valid
    def performe_move(self, move, player, rule):
        if not self.is_valid(player, move):
            raise ValueError
            return
        # Must copy the passedArray so we don't alter the original
        array = deepcopy(self.square_matrix)
        # Set colour and set the moved location to be that colour
        colour = player.color
        array[move[0]][move[1]] = colour

        # Determining the neighbours to the square
        neighbours = []
        for i in range(max(0, move[0] - 1), min(move[0] + 2, self.size[0])):
            for j in range(max(0, move[1] - 1), min(move[1] + 2, self.size[1])):
                if array[i][j] != None:
                    neighbours.append([i, j])
        neighbours.remove(move)

        # Which tiles to convert
        convert = []

        # For all the generated neighbours, determine if they form a line
        # If a line is formed, we will add it to the convert array
        for neighbour in neighbours:
            neighX = neighbour[0]
            neighY = neighbour[1]
            # Check if the neighbour is of a different colour - it must be to form a line
            if array[neighX][neighY] != colour:
                # The path of each individual line
                path = []

                # Determining direction to move
                deltaX = neighX - move[0]
                deltaY = neighY - move[1]

                tempX = neighX
                tempY = neighY

                # While we are in the bounds of the board
                while 0 <= tempX < self.size[0] and 0 <= tempY < self.size[1]:
                    path.append([tempX, tempY])
                    value = array[tempX][tempY]
                    # If we reach a blank tile, we're done and there's no line
                    if value == None:
                        break
                    # If we reach a tile of the player's colour, a line is formed
                    if value == colour:
                        # Append all of our path nodes to the convert array
                        for node in path:
                            convert.append(node)
                        break
                    # Move the tile
                    tempX += deltaX
                    tempY += deltaY

        # Convert all the appropriate tiles
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