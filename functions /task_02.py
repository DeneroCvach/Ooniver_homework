# Напишите программу, которая считает факториал для числа n.
# Например: факториал 5, это 5 * 4 * 3 * 2 * 1


def factorial(n):
    multiply = 1
    for i in range(1, n+1):
        multiply *= i
    return multiply


# Создаем функцию, которая принимает на вход неопределенное количество аргументов и
# возвращает сумму элемента умноженного на его индекс
# например: (2, 5, 6, 7) -> 2 * 0 + 5 * 1 + 6 * 2 + 7 * 3


def sum_func(*args):
    s = 0
    for i in range(len(args)):
        s += args[i] * i

    return s


# Создайте функцию, которая принимает на вход неопределенное количество именованных аргументов
# и печатает в консоль только те, длина ключа у которых кратна 2

def multiple_func(**kwargs):
    for key, value in kwargs.items():
        if not len(value) % 2:
            print(value, end=' ')


def main():
    print(f'Factorial equals -> {factorial(3)}')
    print()
    result = sum_func(2, 5, 6, 7)
    print(f'Sum is -> {result}')
    print()
    print(multiple_func(a='C++', b='Python', c='so', d='boring(', e='cool', f='!!<3'))
    print()


if __name__ == '__main__':
    main()
