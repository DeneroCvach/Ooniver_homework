from point import Point


class Line:
    a: Point
    b: Point

    def __init__(self, point_a: Point, point_b: Point):
        self.a: Point = point_a
        self.b: Point = point_b

    def __str__(self):
        return f'Line from {self.a} to {self.b}'

    def find_length(self):
        side_a = self.b.x - self.a.x
        side_b = self.b.y - self.a.y
        side_a_b = (side_a ** 2 + side_b ** 2) ** 0.5

        return round(side_a_b, 3)


class Square:
    def __init__(self, point_a, point_b):
        self.a = point_a
        point_c = Point(point_a.x, point_b.y)
        self.c = point_c
        self.b = point_b
        point_d = Point(point_b.x, point_a.y)
        self.d = point_d

    def __str__(self):
        return f'Square: A - {self.a}, B - {self.b}, C - {self.c}, D - {self.d}'

    def find_side_line(self):
        side_a_d = self.b.x - self.a.x

        return side_a_d

    def calc_square_perimetr(self):
        perimetr = self.find_side_line() * 4

        return round(perimetr, 3)

    def calc_square_area(self):
        area = self.find_side_line() ** 2

        return round(area, 3)


class Triangle:
    def __init__(self, point_a, point_b, point_c):
        self.a = point_a
        self.b = point_b
        self.c = point_c

    def __str__(self):
        return f'Triangle: A - {self.a}, B - {self.b}, D - {self.c}'

    def find_triangle_sides_length(self):
        side_a_b = ((self.b.x - self.a.x) ** 2 + (self.b.y - self.a.y) ** 2) ** 0.5
        side_b_c = ((self.b.x - self.c.x) ** 2 + (self.b.y - self.c.y) ** 2) ** 0.5
        side_a_c = ((self.c.x - self.a.x) ** 2 + (self.c.y - self.a.y) ** 2) ** 0.5

        return side_a_b, side_b_c, side_a_c

    def calc_triangle_perimetr(self):
        side_1, side_2, side_3 = self.find_triangle_sides_length()
        perimetr = side_1 + side_2 + side_3

        return round(perimetr, 3)

    def calc_triangle_square(self):
        side_1, side_2, side_3 = self.find_triangle_sides_length()
        p = self.calc_triangle_perimetr() / 2
        square = (p * (p - side_1) * (p - side_2) * (p - side_3)) ** 0.5

        return round(square, 3)


class Rectangle:
    def __init__(self, point_a, point_e):
        self.a = point_a
        point_f = Point(point_a.x, point_e.y)
        self.f = point_f
        self.e = point_e
        point_d = Point(point_e.x, point_a.y)
        self.d = point_d

    def __str__(self):
        return f'Rectangle: A - {self.a}, E - {self.e}, F - {self.f}, D - {self.d}'

    def find_rectangle_lines(self):
        side_a_d = self.e.x - self.a.x
        side_e_d = self.e.y - self.a.y

        return side_a_d, side_e_d

    def calc_rectangle_perimetr(self):
        side_1, side_2 = self.find_rectangle_lines()
        perimetr = side_1 * 2 + side_2 * 2

        return round(perimetr, 3)

    def calc_rectangle_square(self):
        side_1, side_2 = self.find_rectangle_lines()
        square = side_1 * side_2

        return round(square, 3)
