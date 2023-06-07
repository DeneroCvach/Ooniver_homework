with open('poem.txt') as file:
    counter = 0
    while row := file.readline():
        print(row)
        counter += 1
        if counter == 4:
            break
