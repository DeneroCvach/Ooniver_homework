my_file = open('poems.txt')
while True:
    line = my_file.readline()
    if not line:
        break
    print(line, end=' ')
my_file.close()
