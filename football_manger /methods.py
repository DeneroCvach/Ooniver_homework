from models import *
from sqlalchemy.orm import sessionmaker
from engine import engine
from models import Football_team, Player


def create_session(data):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(data)
    session.commit()


def add_football_team(name, players_count):
    team = Football_team(name, players_count)
    create_session(team)


def add_player(firstname, lastname, age, high, speed):
    player = Player(firstname, lastname, age, high, speed)
    create_session(player)
