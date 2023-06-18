from random import randint
import json


def generate_square_matrix(n):
    new_matrix = [[randint(1, 100) for _ in range(n)] for _ in range(n)]

    return new_matrix


def find_golden_middle(new_matrix, n):
    golden_middle = []

    for i in range(n):
        golden_middle.append(new_matrix[i][i])

    return golden_middle


def json_file(golden_middle):
    with open('new_json_golden_middle.json', 'w') as new_json:
        golden_data = json.dumps(golden_middle)
        new_json.write(golden_data)


def main():
    n = 5

    new_matrix = generate_square_matrix(n)

    print('Matrix:')
    for row in new_matrix:
        print(row)

    golden_middle = find_golden_middle(new_matrix, n)
    print('\nGolden middle:')
    print(golden_middle)

    json_file(golden_middle)


if __name__ == '__main__':
    main()
