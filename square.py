from disk import Disk

class Square():
    '''repr the location on the board'''

    """
    inner colors dictionary
    
    colors on empty squeres:
    
    colors on connections: 
    dark_light = 4 - full dark and then light
    light_dark = 5 - full light and then dark
    DARK = 1 - only dark members 
    LIGHT = 2 - only light members
    NONE = 0 - no one around
    """
    changed_disks = []
    NONE = 0
    DARK = 1
    LIGHT = 2
    both = 3
    dark_light = 4
    light_dark = 5

    def __init__(self, x, y):
        self.color = self.NONE
        self.up = [None, self.NONE]
        self.left = [None, self.NONE]
        self.right = [None, self.NONE]
        self.down = [None, self.NONE]
        self.diagonal_lu = [None, self.NONE]
        self.diagonal_ld = [None, self.NONE]
        self.diagonal_ru = [None, self.NONE]
        self.diagonal_rd = [None, self.NONE]

        self.x = x
        self.y = y

    def get_neighbours(self):
        return {0: self.up, 1: self.left, 2: self.right, 3: self.down, 4: self.diagonal_lu,
                           5: self.diagonal_ld, 6: self.diagonal_ru, 7: self.diagonal_rd}
    def get_reverse(self,connection):
        reverse ={0:3,1:2, 2:1, 3:0, 4:7, 5:6,6:5,7:4}
        it = self.get_neighbours()[connection][0].get_neighbours()[reverse[connection]]
        return it
    def get_disk_connection(self, connection):
        return self.get_neighbours()[connection]
    def flip_disk(self, flipping_rule, player):
        flipping_rule(self, player.color)


    def change_color(self, new_color):
        self.changed_disks.append(self)
        self.color = new_color
        for i in self.get_neighbours():
            self.update_connection(i)

    def empty_changed_field(self):
        self.changed_disks = []


    def concatenate_flip(self, color, connection, changing_color):
        if self.get_neighbours()[connection] is None:
            return
        tmp = self.get_neighbours()[connection][0]
        while tmp.color == changing_color:
            tmp.change_color(color)
            tmp = self.get_neighbours()[connection][0]



    def update_connection(self, connection, concat_color = None):
        reverse = {0: 3, 1: 2, 2: 1, 3: 0, 4: 7, 5: 6, 6: 5, 7: 4}
        if self.get_neighbours()[connection][0] is None:
            return
        if self.get_disk_connection(connection)[0] is None:
            return

        self.changed_disks.append(self.get_disk_connection(connection)[0])
        if self.color is Square.LIGHT or concat_color is Square.LIGHT:
            # if he look at me and see dark
            if self.get_reverse(connection)[1] is self.DARK:
                self.get_disk_connection(connection)[0].get_reverse(connection)[1] = self.light_dark
                concat = self.get_disk_connection(connection)[0]
                concat.update_connection(connection, concat_color=self.LIGHT)
            else:
                self.get_disk_connection(connection)[0].get_neighbours()[reverse[connection]][1] = self.LIGHT
        else:
            if self.get_reverse(connection)[1] is self.LIGHT:
                self.get_disk_connection(connection)[0].get_reverse(connection)[1] = self.dark_light
                concat = self.get_disk_connection(connection)[0]
                concat.update_connection(connection, concat_color=self.DARK)
            else:
                self.get_disk_connection(connection)[0].get_neighbours()[reverse[connection]][1] = self.DARK

    def get_up(self):
        return self.up


    def get_down(self):
        return self.down


    def get_left(self):
        return self.left


    def get_right(self):
        return self.right


    def get_diagonal_lu(self):
        return self.diagonal_lu


    def get_diagonal_ld(self):
        return self.diagonal_ld


    def get_diagonal_ru(self):
        return self.diagonal_ru


    def get_diagonal_rd(self):
        return self.diagonal_rd