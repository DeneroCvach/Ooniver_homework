from datetime import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import SmallInteger, String, ForeignKey


class Base(DeclarativeBase):
    pass


class Football_team(Base):
    __tablename__ = 'team'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30))
    players_count: Mapped[int] = mapped_column(SmallInteger)
    created: Mapped[datetime] = mapped_column(insert_default=datetime.now())

    def __init__(self, name, players_count):
        self.name = name
        self.players_count = players_count


class Player(Base):
    __tablename__ = 'player'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    firstname: Mapped[str] = mapped_column(String(30))
    lastname: Mapped[str] = mapped_column(String(40))
    age: Mapped[int] = mapped_column(SmallInteger)
    high: Mapped[int] = mapped_column(SmallInteger)
    team_id: Mapped[int] = mapped_column(ForeignKey("team.id"), nullable=True)
    speed: Mapped[int] = mapped_column(SmallInteger)
    create_date: Mapped[datetime] = mapped_column(insert_default=datetime.now())

    def __init__(self, firstname, lastname, age, high, speed):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.high = high
        self.speed = speed
