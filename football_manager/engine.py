from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

HOST = 'localhost'
PORT = '5432'
USER = 'postgres'
PASSWORD = 'postgres'
DB_NAME = 'football manager'

engine = create_engine(f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}/{DB_NAME}')

if not database_exists(engine.url):
    create_database(engine.url)
