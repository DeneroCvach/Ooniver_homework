try:
    c = int(input('a = ')) / int(input('b = '))
except (ZeroDivisionError, ValueError) as e:
    print(f'U got mistake {e}')
    print('Send message to dev..')
