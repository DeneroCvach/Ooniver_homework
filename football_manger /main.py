from methods import *


def main():
    # start = input('Add team or player?')
    # if start:
    #     if start == 'team':
    #         name = input('Enter team name: ')
    #         players_count = input('Enter players count: ')
    #
    #         add_football_team(name, players_count)
    #
    #     if start == 'players':
    #         firstname = input('Enter player firstname: ')
    #         lastname = input('Enter player lastname: ')
    #         age = input('Enter player age: ')
    #         high = input('Enter player high: ')
    #         speed = input('Enter player speed: ')
    #
    #         add_player(firstname, lastname, age, high, speed)
    # else:
    #     print('Enter somthing u work with!')
    # add_player('Mario', 'Balatelli', 27, 190, 32)
    add_football_team('FC Minsk', 30)
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    main()
