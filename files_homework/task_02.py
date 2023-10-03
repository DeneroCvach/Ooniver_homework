# Напишите программу, которая спрашивает вас которую по счёту строку вывести в консоль,
# строки считаются от 1. Если строки не существует, выводит предупреждение об этом и спрашивает опять.
# Если ввели 0 - выводит весь файл в консоль и завершает программу.

def output_line():
    with open('poem.txt') as file:
        row_list = []
        while row := file.readline():
            row_list.append(row)
    return row_list


def all_text():
    with open('poem.txt') as file:
        text = file.read()
        print(text)
        file.close()


def main():
    while True:
        num = int(input('Enter line number(0 - for entire text): '))
        print()
        if num > len(output_line()):
            print('Out of range...\nTry again!')
        elif num == 0:
            all_text()
            break
        else:
            line = output_line()
            print(line[num-1])



if __name__ == '__main__':
    main()
