# Написать программу, которая запрашивает у пользователя фразу или слово
# и проверяет, является ли это палиндромом. Пример палиндромов: “шалаш”, “а роза упала на лапу Азора”, “101”

def palindrome_check(word):
    word = word.replace(' ', '').lower()
    if word == word[::-1]:
        return True
    else:
        return False


def main():
    phrase = input('Enter word or phrase: ')

    if palindrome_check(phrase):
        print(f'{phrase} is palindrome!')
    else:
        print(f"{phrase} isn't palindrome!")


if __name__ == '__main__':
    main()
