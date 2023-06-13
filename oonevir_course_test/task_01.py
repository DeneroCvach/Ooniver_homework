number = int(input('Enter your number.. '))

for i in range(1, number + 1):
    if not number % i:
        print(i)
