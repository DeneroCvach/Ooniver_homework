def decorator(func):
    def wrapper():
        print('Функция-обёртка!')
        print(f'Оборачиваемая функция: {func}')
        print('Выполняем обёрнутую функцию...')
        # действия до
        func()
        # действия после
        print('Выходим из обёртки')

    return wrapper


@decorator
def say_hello():
    print('say hello')

say_hello()
