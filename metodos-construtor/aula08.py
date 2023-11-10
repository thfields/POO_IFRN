class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class Circle:
    def __init__(self, radius, center) -> None:
        self.radius = radius
        self.center = center

centro = Point(150,100)
c1 = Circle(75, centro)

 