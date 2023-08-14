from point import Point


class Line:

    def __init__(self, point_a: Point, point_b: Point):
        self.a = point_a
        self.b = point_b

    def distance(self):
        side_a = self.b.x - self.a.x
        side_b = self.b.y - self.a.y
        side_c = (side_a ** 2 + side_b ** 2) ** 0.5
        return side_c

    def __str__(self):
        return f'Line ({self.a}.{self.b})'


class Square:
    def __init__(self, point_a, point_c):
        self.a = point_a
        point_b = Point(point_a.x, point_c.y)
        self.b = point_b
        self.c = point_b
        point_d = Point(point_c.x, point_a.y)
        self.d = point_d
