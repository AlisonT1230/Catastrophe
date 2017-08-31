from cat import Cat

MAX_KNEAD = 100
MAX_HEALTH = 100
MAX_LIVES = 5

class Player(Cat):

    def __init__(self, x, y):
        super(Player, self).__init__(x, y, 'black')
        self.health = 100
        self.lives = 5
        self.knead_power = 0
        self.kneading = False
        self.on_blanket = False
        self.grounded = False
    
    
    def update(self, count, boundary_x, boundary_y):
        self.update_position(boundary_x, boundary_y)
        self.update_img(count)
        self.__update_knead_val()
    

    def move_left(self):
        self.dx = -10


    def move_right(self):
        self.dx = 10


    def stop(self):
        self.dx = 0


    def jump(self):
        if self.y == self.ground_height and not self.kneading:
            self.dy = -20
            self.jump_sound.play()


    def knead(self):
        if self.knead_power < MAX_KNEAD and self.y == self.ground_height and self.on_blanket:
            self.kneading = True
            self.purr_sound.play(-1)
        

    def stop_knead(self):
        self.kneading = False
        self.purr_sound.fadeout(1000)


    def add_health(self, amt):
        if self.health + amt < MAX_HEALTH:
            self.health += amt
        else:
            self.health = MAX_HEALTH


    def drop_health(self, amt):
        if self.health - amt > 0:
            self.health -= amt
        else:
            self.health = 0
            self.drop_life()

    
    def add_life(self):
        if self.lives < MAX_LIVES:
            self.lives += 1


    def drop_life(self):
        if self.lives > 0:
            self.lives -= 1
        else:
            pass
            #   GAME OVER


    def __update_knead_val(self):
        if self.kneading:
            if self.knead_power < MAX_KNEAD:
                self.knead_power += 0.5
            else:
                self.stop_knead()
