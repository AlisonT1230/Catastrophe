import settings

class Cat:

    def __init__(self, x, y, col):
        self.x, self.y, self.dx, self.dy = x, y, 0, 0
        self.width, self.height = 100, 100
        self.img_src = "textures/cats/" + col + "_cat.bmp"
    
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