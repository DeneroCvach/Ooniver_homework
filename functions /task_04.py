# Напишите программу для вычисления квадратных уравнений.

def quadratic_equation(a, b, c):
    x1 = x2 = 0

    d = (b ** 2) - (4 * a * c)

    if d != 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return x1, x2
    elif d == 0:
        x1 = x2 = -b / (2 * a)

        return x1, x2
    else:
        return None


def main():
    root1, root2 = quadratic_equation(5, 3, -26)
    if equation_data is None:
        print('no solutions...')
    else:
        print('the solution(s) to the equation is', root1, root2)


if __name__ == '__main__':
    main()

