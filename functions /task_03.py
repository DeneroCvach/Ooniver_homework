# Напишите программу, которая принимает неопределенное количество аргументов
# и именованный параметр action, значения для него: ‘+’ или ‘*’,
# что значит нужно вернуть сумму или произведение из переданных аргументов.
# Реализовать тремя функциями.


def sum_func(*args):
    s = 0
    for i in args:
        s += i
    return s


def mult_func(*args):
    m = 1
    for i in args:
        m *= i
    return m


def result_func(action, *args):
    if action == '+':
        return sum_func(*args)
    elif action == '*':
        return mult_func(*args)


def main():
    action = input('Choose operation -> + or *: ')
    print()
    data = result_func(action, 2, 4, 6, 8)
    if data is not None:
        print(f'Operation result is -> {data}')
    else:
        print('Invalid value of operation...')


if __name__ == '__main__':
    main()
