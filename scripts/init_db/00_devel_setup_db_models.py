import src
from src.models import Base

# Drops and recreates DB
engine, Session = src.db_connection(init=False)
Base.metadata.drop_all(engine)
Base.metadata.create_all(bind=engine)