from ground import Ground

class GroundManager:

    def __init__(self):
        self.blankets = []
        self.ground_blocks = []
        
    def build_group(self, x1, y1, x2, y2, type):
        """
        Builds a collection of type ground blocks according to x and y coordinates.
        """
        for x in range (x1, x2 + 100, 100):
            for y in range (y1, y2 + 100, 100):
                self.ground_blocks.append(Ground(x, y, type))
                