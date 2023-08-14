# Создать декоратор для функции, которая принимает на вход неопределенное количество аргументов.
# Декоратор должен перевернуть аргументы для функции в обратном порядке.

def reverse_arguments(func):
    def wrapper(*args):
        reverse_args = args[::-1]
        return func(*reverse_args)
    return wrapper


@reverse_arguments
def func(*args):
    return args


result = func(1, 2, 3, 4, 5)
print(result)
