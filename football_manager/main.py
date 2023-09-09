from methods import *

Base.metadata.create_all(engine)


def main():
    session = Session(bind=engine)
    Player.add_player(session, 'Mario', 'Balatelli', 27, 190, 32)
    Football_team.add_football_team(session, 'FC Minsk')


if __name__ == '__main__':
    main()
