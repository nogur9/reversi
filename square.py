from disk import Disk

class Square(Disk):
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
    both = 3
    dark_light = 4
    light_dark = 5

    def __init__(self, x, y):
        self.color = self.NONE
        self.up = None
        self.left = None
        self.right = None
        self.down = None
        self.diagonal_lu = None
        self.diagonal_ld = None
        self.diagonal_ru = None
        self.diagonal_rd = None
        self.neighbours = [self.up, self.left, self.right, self.down, self.diagonal_lu,
                           self.diagonal_ld, self.diagonal_ru, self.diagonal_rd]
        self.x = x
        self.y = y

    def flip_disk(self, flipping_rule, player):
        flipping_rule(self, player.color)


    def change_color(self, new_color):
        self.changed_disks.append(self)
        self.color = new_color
        self.update_connection(self.get_diagonal_ld)
        self.update_connection(self.get_diagonal_lu)
        self.update_connection(self.get_diagonal_rd)
        self.update_connection(self.get_diagonal_ru)
        self.update_connection(self.get_up)
        self.update_connection(self.get_down)
        self.update_connection(self.get_left)
        self.update_connection(self.get_right)


    def empty_changed_field(self):
        self.changed_disks = []


    def concatenate_flip(self, color, connection, changing_color):
        tmp = connection(self)[0]
        while tmp.color == changing_color:
            tmp.change_color(color)
            tmp = connection(tmp)[0]



    def update_connection(self, connection):
        if self.color is Disk.LIGHT:
            if connection(self)[1] is self.DARK:
                # if full dark, and light- update neighbour to light and all the others toward dark_light
                connection(self)[1] = self.LIGHT
                self.changed_disks.append(connection(self)[0])
                tmp = connection(self)[0]
                while connection(tmp)[1] is self.DARK:
                    connection(tmp)[1] = self.dark_light
                    self.changed_disks.append(tmp)
                    tmp = connection(tmp)[0]

            elif connection(self)[1] is self.LIGHT:
                # if full light, and light-dont update
                pass
            elif connection(self)[1] is self.NONE:
                connection(self)[1] = self.LIGHT
                self.changed_disks.append(connection(self)[0])
                tmp = connection(self)[0]
                while connection(tmp)[1] is self.DARK:
                    connection(tmp)[1] = self.dark_light
                    self.changed_disks.append(tmp)
                    tmp = connection(tmp)[0]
            elif connection(self)[1] is self.dark_light:
                self.changed_disks.append(connection(self)[0])
                connection(self)[1] = self.LIGHT
        if self.color is Disk.DARK:
            if self.connection()[1] is self.LIGHT:
                # if full light, and dark-
                self.connection()[1] = self.DARK
                self.changed_disks.append(connection(self)[0])
                tmp = self.connection()[0]
                while tmp.connection()[1] is self.LIGHT:
                    tmp.connection()[1] = self.light_dark
                    self.changed_disks.append(tmp)
                    tmp = tmp.connection()[0]
            elif self.connection()[1] is self.DARK:
                # if full light, and light-dont update
                pass
            elif self.connection()[1] is self.NONE:
                self.connection()[1] = self.DARK
                self.changed_disks.append(connection(self)[0])
                tmp = self.connection()[0]
                while tmp.connection()[1] is self.LIGHT:
                    tmp.connection()[1] = self.light_dark
                    self.changed_disks.append(tmp)
                    tmp = tmp.connection()[0]
            elif self.connection()[1] is self.light_dark:
                self.changed_disks.append(connection(self)[0])
                self.connection()[1] = self.DARK


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