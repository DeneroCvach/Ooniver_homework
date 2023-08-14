# Создать декоратор для функции, которая принимает на вход список чисел. Декоратор должен переводить в строку
# каждый второй элемент списка.

numbers_list = [1, 2, 3, 4, 5, 6]


def convert_even_indices_to_string(func):
    def wrapper(numbers):
        converted_numbers = list(map(lambda number: str(number) if numbers.index(number) % 2 == 1 else number, numbers_list))
        return func(converted_numbers)
    return wrapper


@convert_even_indices_to_string
def numbers(numbers):
    return numbers


result = numbers(numbers_list)
print(result)
