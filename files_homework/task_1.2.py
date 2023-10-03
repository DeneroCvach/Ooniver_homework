with open('poem.txt') as file:
    counter = 0
    while row := file.readline():
        counter += 1
        if not counter % 3:
            print(row)
