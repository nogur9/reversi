from disk import Disk
from square import Square

class Board:
    '''the game board'''

    def __init__(self, size, ysize=0):
        self.search_pool = []
        if ysize:
            self.size = (size, ysize)
        else:
            self.size = (size, size)
        self.square_matrix = []
        for x in range(self.size[0]):
            self.square_matrix.append([])
            for y in range(self.size[1]):
                self.square_matrix[x].append(Square(x, y))
                self.update_connection(x, y)

    def update_connection(self, x, y):
        if x > 0:
            self.square_matrix[x][y].left = [self.square_matrix[x-1][y], Square.NONE]
            self.square_matrix[x-1][y].right = [self.square_matrix[x][y], Square.NONE]

        if y > 0:
            self.square_matrix[x][y].up = [self.square_matrix[x][y-1],Square.NONE]
            self.square_matrix[x][y-1].down = [self.square_matrix[x][y],Square.NONE]

        if x > 0 and y > 0:
            self.square_matrix[x][y].diagonal_lu = [self.square_matrix[x-1][y-1], Square.NONE]
            self.square_matrix[x-1][y-1].diagonal_ru = [self.square_matrix[x][y], Square.NONE]

        if y < (self.size[0] - 1) and x>0:
            self.square_matrix[x - 1][y + 1].diagonal_rd = [self.square_matrix[x][y], Square.NONE]
            self.square_matrix[x][y].diagonal_ld = [self.square_matrix[x-1][y + 1], Square.NONE]

    def init_starting_pattern(self, rule):
        """useless for now"""
        pass


    def flip_disk (self, move, rule, player):
        '''save changed disks and return the move disk'''
        '''flipping_rule'''
        ''':exception your problem'''
        self.square_matrix[move[0]][move[1]].flip_disk(rule, player)
        #print(*([s.x,s.y] for s in Square.changed_disks))
        self.update_search_pool()

    def update_search_pool(self):
        '''look at changed field of the disks and update accordingly'''
        disk: Square
        for disk in Square.changed_disks:
            if not (disk.color == Square.NONE):
                try:
                    self.search_pool.remove(disk)
                except ValueError:
                    pass
            else:
                if disk not in self.search_pool:
                    self.search_pool.append(disk)

    def get_square_matrix(self):
        return self.square_matrix


    def get_search_pool(self):
        return self.search_pool


    def display_board(self):
        #TODO UI
        # useless
        pass

