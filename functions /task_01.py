# Напишите программу, которая умеет:
# 1 создавать матрицу заданных размеров n и m
# 2 выводить её на экран
# 3 находить наибольшее и наименьшее значения
# 4 сортировать по возрастанию и по убыванию матрицы
# 5 если матрица квадратная (равное количество столбцов и строк), то говорит об этом


from random import randint


def create_matrix(n, m):
    matrix = []
    for _ in range(n):
        row = []
        for _ in range(m):
            row.append(randint(10, 99))
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(row)


def increase_sort_matrix(matrix):
    sorted_matrix = []
    for row in matrix:
        increase_sorted_row = sorted(row)
        sorted_matrix.append(increase_sorted_row)
    return sorted_matrix


def descending_sort_matrix(matrix):
    sort_matrix = []
    for row in matrix:
        descending_sorted_row = sorted(row, reverse=True)
        sort_matrix.append(descending_sorted_row)
    return sort_matrix


def min_max_elem(matrix):
    min_elem = matrix[0][0]
    max_elem = matrix[0][0]
    for row in matrix:
        for elem in row:
            if elem > min_elem:
                min_elem = elem
            if elem < max_elem:
                max_elem = elem
    return min_elem, max_elem


def square_matrix(matrix):
    if len(matrix) == len(matrix[0]):
        print('MATRIX IS SQUARE')


def main():
    matrix = create_matrix(n=int(input('Enter the number of rows: ')), m=int(input('Enter the number of columns: ')))
    print_matrix(matrix)
    print()
    max_elem, min_elem = min_max_elem(matrix)
    print(f'Max matrix elem -> {max_elem} \nMin matrix elem -> {min_elem}')
    print()
    print(square_matrix(matrix))


if __name__ == '__main__':
    main()
