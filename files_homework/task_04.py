# Напишите программу которая спрашивает что сделать, записать файл по новому или дописать,
# после чего начинает запись строк текста, текст вводится с клавиатуры до тех пор,
# пока не введено ключевое слово-команда “/стоп”. Запись в файл прекращается

def write_file(file_mode):
    with open('some_text.txt', file_mode) as file:
        print('Enter your text(for exit enter /stop)')
        while True:
            data = input()
            if data == '/stop':
                break
            file.write(data + '\n')


def main():
    start = input('Chose write mode: add or rewrite?.. ')
    if start == 'add':
        file_mode = 'a'
        write_file(file_mode)
    elif start == 'rewrite':
        file_mode = 'w'
        write_file(file_mode)
    else:
        print('Wrong command!!! Try again!')


if __name__ == '__main__':
    main()
