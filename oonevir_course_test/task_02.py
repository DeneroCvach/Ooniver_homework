def reverse_line(line):
    words = line.split()
    reversed_words = words[::-1]
    reversed_line = ' '.join(reversed_words)

    return reversed_line


def main():
    line = input('Enter your line.. ')
    print(line)
    reversed_line = reverse_line(line)
    print(reversed_line)


if __name__ == '__main__':
    main()
