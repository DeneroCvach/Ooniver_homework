with open('poem.txt') as file:
    row_list = []
    n = 0
    m = 1
    while row := file.readline():
        row_list.append(row)
    print(*row_list[n:m])
