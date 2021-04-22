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


def spark_session():
    from pyspark.sql import SparkSession

    spark = (
        SparkSession.builder.master(f"local[{config.get('Spark', 'n_cores')}]")
        .appName("pppd")
        .config("spark.submit.deployMode", "client")
        .config("spark.shuffle.spill.compress", "false")
        .config("spark.driver.memory", config.get('Spark', 'driver_mem'))
        .config("spark.executor.memory",  config.get('Spark', 'exec_mem'))
        .config("spark.driver.maxResultSize",  config.get('Spark', 'max_resultsize'))
        .getOrCreate()
    )

    return spark