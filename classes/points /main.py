from point import Point
from figures import Line, Square

if __name__ == '__main__':
    point_a = Point(1, 1)
    point_b = Point(4, 3)
    print(point_a, point_b)
    line_1 = Line(point_a, point_b)
    print(line_1)
    line_1.distance()
    square_1 = Square(point_a, point_b)
