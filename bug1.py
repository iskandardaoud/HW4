from shape import Shape
from circle import Circle

class Base(Shape):
    pass

class Circle(Base):
    pass

def main():
    c = Circle(1, 2, 3)
    print(c.shape())
    print(c.draw())

if __name__ == '__main__':
    main()
