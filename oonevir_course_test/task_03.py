def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


def main():
    number = int(input('enter ur number: '))
    result = factorial(number)
    print(result)


if __name__ == '__main__':
    main()
