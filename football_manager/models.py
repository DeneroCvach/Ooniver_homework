from datetime import datetime
from typing import List


from engine import engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import SmallInteger, String, ForeignKey, Integer


class Base(DeclarativeBase):
    pass


class Football_team(Base):
    __tablename__ = 'team'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30))
    players_count: Mapped[int] = mapped_column(SmallInteger, insert_default=0)
    created: Mapped[datetime] = mapped_column(insert_default=datetime.now())
    players: Mapped[List["Player"]] = relationship(back_populates="team")

    def __init__(self, name):
        self.name = name

    @classmethod
    def add_football_team(cls, session, name):
        team = Football_team(name)
        session.add(team)
        session.commit()


class Player(Base):
    __tablename__ = 'player'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    firstname: Mapped[str] = mapped_column(String(30))
    lastname: Mapped[str] = mapped_column(String(40))
    age: Mapped[int] = mapped_column(SmallInteger)
    high: Mapped[int] = mapped_column(SmallInteger)
    speed: Mapped[int] = mapped_column(SmallInteger)
    team_id: Mapped[int] = mapped_column(Integer(), ForeignKey("team.id"), nullable=True)
    create: Mapped[datetime] = mapped_column(insert_default=datetime.now())
    team: Mapped['Football_team'] = relationship(back_populates="players")

    def __init__(self, firstname, lastname, age, high, speed):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.high = high
        self.speed = speed

    @classmethod
    def add_player(cls, session, firstname, lastname, age, high, speed):
        player = Player(firstname, lastname, age, high, speed)
        session.add(player)
        session.commit()
