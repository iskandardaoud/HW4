from shape import shape

class circle(shape):
    def __init__(self, x, y, size):
        super().__init__(x, y, size)

    def draw(self):
        return f'Circle at ({self.x}, {self.y}) with radius {self.size}'
