from configparser import ConfigParser
from pathlib import Path

PATH = Path(__file__).parent.parent


config = ConfigParser()
config.read(Path.joinpath(PATH, "config.ini"))

try:
    user = config.get("DB", "POSTGRES_USER")
    pwd = config.get("DB", "POSTGRES_PASSWORD")
    host = config.get("DB", "POSTGRES_HOST")
    port = config.get("DB", "POSTGRES_PORT")
    database = config.get("DB", "POSTGRES_DB")

    CONN = f"postgresql+psycopg2://{user}:{pwd}@{host}:{port}/{database}"

except Exception as error:
    print("WARNING: No connection to Database.")
    print(error)


def db_connection(init=True):
    """returns DB connection as engine, session tuple if init=False, session is sessionmaker instance"""
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(CONN)
    Session = sessionmaker(bind=engine)

    if init:
        return engine, Session()
    return engine, Session

