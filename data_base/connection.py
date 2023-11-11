from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine("postgresql+psycopg2://postgres:787898@localhost/TG_BOT")


def get_db_session():
    return Session(bind=engine)
