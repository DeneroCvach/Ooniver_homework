from point import Point
from figures import Line, Square, Triangle, Rectangle

if __name__ == '__main__':
    point_a = Point(1, 1)
    point_b = Point(9, 9)
    point_e = Point(9, 5)
    point_c = Point(4, 7)
    print(point_a, point_b, point_e, point_c)
    print()

    line_1 = Line(point_a, point_b)
    print(line_1)
    print(f'Length of line - {line_1.find_length()}')
    print()

    square_1 = Square(point_a, point_b)
    print(square_1)
    square_perimetr = Square.calc_square_perimetr(square_1)
    print(f'Square perimetr - {square_perimetr}')
    square_area = Square.calc_square_area(square_1)
    print(f'Square area - {square_area}')
    print()

    triangle_1 = Triangle(point_a, point_b, point_c)
    print(triangle_1)
    triangle_perimetr = Triangle.calc_triangle_perimetr(triangle_1)
    print(f'Triangle perimetr - {triangle_perimetr}')
    triangle_square = Triangle.calc_triangle_square(triangle_1)
    print(f'Triangle square - {triangle_square}')
    print()

    rectangle_1 = Rectangle(point_a, point_e)
    print(rectangle_1)
    rectangle_perimetr = Rectangle.calc_rectangle_perimetr(rectangle_1)
    print(f'Rectangle perimetr - {rectangle_perimetr}')
    rectangle_square = Rectangle.calc_rectangle_square(rectangle_1)
    print(f'Rectangle square - {rectangle_square}')
