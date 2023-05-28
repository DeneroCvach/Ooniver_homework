# Напишите программу, которая умеет переводить одни величины в другие:
# градусы цельсия в фаренгейты, мили в километры, километры в метры, морские мили в километры, километры в футы.
# Программы при запуске спрашивает у пользователя, что ей сделать и потом работает с входными данными.
# Сделайте так, чтобы пользователь мог пользоваться программой столько, сколько нужно, пока не решит выйти из программы,
# выбрав соответствующий пункт.

from art import tprint


def celsius_to_fahrenheit(c):
    c = (c * 9/5) + 32
    return c


def mile_to_kilometer(m):
    m *= 1.60934
    return m


def kilometer_to_meter(k):
    k *= 1000
    return k


def sea_miles_to_kilometer(sm):
    sm /= 1.852
    return sm


def kilometer_to_feet(f):
    f *= 3281
    return f


def main():
    tprint("Konverter!!!")
    while True:
        print('''
1. Degrees Celsius to Fahrenheit
2. Miles to kilometers
3. Kilometers to meters
4. Sea miles to kilometers
5. Kilometers to feet
6. Quit
'''
)
        operation = int(input('Enter operation number: '))
        print()
        if operation == 6:
            print('You left the program...')
            break
        units = int(input('Enter the sign of the desired value: '))
        print()
        if operation == 1:
            print(celsius_to_fahrenheit(c=units), 'is your converted value!')
        elif operation == 2:
            print(mile_to_kilometer(m=units), 'is your converted value!')
        elif operation == 3:
            print(kilometer_to_meter(k=units), 'is your converted value!')
        elif operation == 4:
            print(sea_miles_to_kilometer(sm=units), 'is your converted value!')
        elif operation == 5:
            print(kilometer_to_feet(f=units), 'is your converted value!')


if __name__ == '__main__':
    main()
