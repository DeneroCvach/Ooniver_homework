# Напишите программу для вычисления квадратных уравнений.

def solve_quadratic_equation(a, b, c):
    # Вычисляем дискриминант
    discriminant = (b**2) - (4*a*c)

    if discriminant > 0:
        x1 = (-1 * b + (discriminant ** 0.5)) / (2*a)
        x2 = (-1 * b - (discriminant ** 0.5)) / (2*a)

        return x1, x2

    elif discriminant == 0:
        x = -b / (2*a)

        return x, x

    else:
        return 0, 0


def main():
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

    solution1, solution2 = solve_quadratic_equation(a, b, c)

    if solution1 == 0 and solution2 == 0:
        print("the equation has no solutions: ")

    elif solution1 == solution2:
        print("the equation has one solution: ")
        print("x =", solution1)

    else:
        print("the equation has two solutions: ")
        print("x1 =", solution1)
        print("x2 =", solution2)


if __name__ == '__main__':
    main()
