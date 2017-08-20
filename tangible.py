class Tangible(object):

    def __init__(self, x, y, width, height):
        """
        Keyword arguments:
        
        x -- x position on screen
        y -- y position on screen
        width -- pixel width
        height -- pixel height
        """
        self.x, self.y, self.width, self.height = x, y, width, height


    def is_collide(self, other_t):
        """
        Returns True if self is within bounds of other tangible.
        Note: Assumes objects are rectangles.

        Keyword arguments:

        other_t -- other tangible
        """
        self_rs = self.x + self.width       #   right side
        self_bs = self.y + self.height      #   bottom side
        other_rs = other_t.x + other_t.width
        other_bs = other_t.y + other_t.height

        return self.__x_collide(self_rs, other_t.x, other_rs) and self.__y_collide(self_bs, other_t.y, other_bs)
        

    def  __x_collide(self, self_rs, other_x, other_rs):
        if self.x >= other_x and self.x <= other_rs:      #   left side intersect
            return True
        elif self_rs >= other_x and self_rs <= other_rs:  #   right side intersect
            return True
        else:                                           #   no collision
            return False


    def __y_collide(self, self_bs, other_y, other_bs):
        if self.y >= other_y and self.y <= other_bs:    #   top side intersect
            return True
        elif self_bs >= other_y and self_bs <= other_bs:     #   bottom side intersect
            return True
        else:                                           #   no collision
            return False
