from shape import Shape

class Circle(Shape):
    def __init__(self, x, y, size):
        super().__init__(x, y, size)

    def draw(self):
        return f'Circle at ({self.x}, {self.y}) with radius {self.size}'
