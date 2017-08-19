import settings

MAX_KNEAD = 100

class Cat:

    def __init__(self, x, y, col):
        self.x, self.y, self.dx, self.dy = x, y, 0, 0
        self.width, self.height = 100, 100
        self.img_src = "textures/cats/" + col + "_cat.bmp"
        self.knead_power = 0

    def update(self):
        if self.dx > 0:
            if self.x < settings.screen_width - self.width:
                self.x += self.dx
            else:
                self.x = settings.screen_width - self.width
        elif self.dx < 0:
            if self.x > 0:
                self.x += self.dx
            else:
                self.x = 0
        if self.dy > 0:
            if self.y < settings.screen_height - self.height:
                self.y += self.dy
            else:
                self.y = settings.screen_height - self.height
        elif self.dy < 0:
            if self.y > 0:
                self.y += self.dy
        self.dy += 1

    def move_left(self):
        self.dx = -10

    def move_right(self):
        self.dx = 10

    def stop(self):
        self.dx = 0

    def jump(self):
        if self.y == settings.screen_height - self.height:
            self.dy = -20

    def knead(self):
        if self.knead_power < MAX_KNEAD:
            self.knead_power += 1