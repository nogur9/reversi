from disk import Disk
from square import Square

class Board:
    '''the game board'''

    def __init__(self, size, ysize=0):
        self.search_pool = []
        if ysize:
            self.size = (size, size)
        else:
            self.size = (size, ysize)
        self.square_matrix = [[]*self.size[1]]*self.size[0]
        for x in self.size[0]:
            for y in self.size[1]:
                self.square_matrix[x][y] = Square(x, y)


    def init_starting_pattern(self, rule):
        """useless for now"""
        pass


    def flip_disk (self, move, rule, player):
        '''save changed disks and return the move disk'''
        '''flipping_rule'''
        ''':exception your problem'''
        self.square_matrix[move[0]][move[1]].flip_disk(rule, player)
        self.update_search_pool()

    def update_search_pool(self):
        '''look at changed field of the disks and update accordingly'''
        disk: Square
        for disk in Square.changed_disks:
            if not (disk.color == Disk.NONE):
                try:
                    self.search_pool.remove(disk)
                except ValueError:
                    pass
            else:
                if disk not in self.search_pool:
                    for connection in disk.neighbours:
                        if connection[1] == disk.light_dark or connection[1] == disk.dark_light:
                            self.search_pool.append(disk)
                            break

    def get_square_matrix(self):
        return self.square_matrix


    def get_search_pool(self):
        return self.search_pool


    def display_board(self):
        #TODO UI
        # useless
        pass

