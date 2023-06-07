# Напишите программу которая сравнивает два файла построчно, если файлы равны по содержанию,
# программа говорит об этом. Если не равны - выводит номера различных строк и их содержимое.
# Усложненная задача:
# * так же выводит позицию (номер символа в строке с отличием)

with open('1.txt') as file1, open('2.txt') as file2:
    rows_1 = file1.readlines()
    rows_2 = file2.readlines()

if rows_1 == rows_2:
    print('y')
else:
    if len(rows_1) > len(rows_2):
        max_len_rows = len(rows_1)
    else:
        max_len_rows = len(rows_2)
    for i in range(max_len_rows):
        row_1 = rows_1[i]
        row_2 = rows_2[i]
        if row_1 != row_2:
            print(f"Line difference {i+1}:")
            print(f"File 1: {row_1}")
            print(f"File 2: {row_2}")
