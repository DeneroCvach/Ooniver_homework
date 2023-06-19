# Напишите программу, которая умеет:
# 1 создавать матрицу заданных размеров n и m
# 2 выводить её на экран
# 3 находить наибольшее и наименьшее значения
# 4 сортировать по возрастанию и по убыванию матрицы
# 5 если матрица квадратная (равное количество столбцов и строк), то говорит об этом


from random import randint


def create_matrix(rows, columns):
    matrix = []
    for _ in range(rows):
        row = []
        for _ in range(columns):
            row.append(randint(10, 99))
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(*row, end='\n')


def increase_sort_matrix(matrix, columns):
    flag = True

    while flag:
        flag = False

        for list_index in range(len(matrix)):
            for elem_index in range(len(matrix[list_index]) - 1):
                if matrix[list_index][elem_index] > matrix[list_index][elem_index + 1]:
                    matrix[list_index][elem_index], matrix[list_index][elem_index + 1] = matrix[list_index][elem_index + 1], matrix[list_index][elem_index]
                    flag = True
        for list_index in range(len(matrix) - 1):
            if matrix[list_index][columns - 1] > matrix[list_index + 1][0]:
                matrix[list_index][columns - 1], matrix[list_index + 1][0] = matrix[list_index + 1][0], matrix[list_index][columns - 1]
                flag = True

    return matrix


def descending_sort_matrix(matrix, columns):
    flag = True

    while flag:
        flag = False

        for list_index in range(len(matrix)):
            for elem_index in range(len(matrix[list_index]) - 1):
                if matrix[list_index][elem_index] < matrix[list_index][elem_index + 1]:
                    matrix[list_index][elem_index], matrix[list_index][elem_index + 1] = matrix[list_index][
                        elem_index + 1], matrix[list_index][elem_index]
                    flag = True
        for list_index in range(len(matrix) - 1):
            if matrix[list_index][columns - 1] < matrix[list_index + 1][0]:
                matrix[list_index][columns - 1], matrix[list_index + 1][0] = matrix[list_index + 1][0], matrix[list_index][columns - 1]
                flag = True

    return matrix


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
    columns = int(input('Enter the number of columns: '))
    rows = int(input('Enter the number of rows: '))
    matrix = create_matrix(rows, columns)
    print_matrix(matrix)
    print()
    max_elem, min_elem = min_max_elem(matrix)
    print(f'Max matrix elem -> {max_elem} \nMin matrix elem -> {min_elem}')
    print()
    print('increase sort matrix')
    print_matrix(increase_sort_matrix(matrix, columns))
    print()
    print('descending sort matrix')
    print_matrix(descending_sort_matrix(matrix, columns))
    print()
    square_matrix(matrix)


if __name__ == '__main__':
    main()
