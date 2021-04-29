from configparser import ConfigParser
from pathlib import Path

PATH = Path(__file__).parent.parent


config = ConfigParser()
config.read(PATH / "config.ini")


user = config.get("DB", "user")
pwd = config.get("DB", "pwd")
host = config.get("DB", "host")
port = config.get("DB", "port")
database = config.get("DB", "database")

CONN = f"postgresql+psycopg2://{user}:{pwd}@{host}:{port}/{database}"


def db_connection(init=True):
    """returns DB connection as engine, session tuple if init=False, session is sessionmaker instance"""
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(CONN)
    Session = sessionmaker(bind=engine)

    if init:
        return engine, Session()
    return engine, Session

