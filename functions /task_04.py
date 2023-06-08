# Напишите программу для вычисления квадратных уравнений.

def quadratic_equation(a, b, c):
    if a == 0:
        return None

    d = (b ** 2) - (4 * a * c)

    if d != 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return x1, x2

    elif d == 0:
        x = -b / (2 * a)
        return x
    else:
        return None


def main():
    equation_data = quadratic_equation(5, 3, -26)

    if equation_data is None:
        print('no solutions...')
    else:
        print('the solution(s) to the equation is', *equation_data)


if __name__ == '__main__':
    main()
