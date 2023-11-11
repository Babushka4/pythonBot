from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine("postgresql+psycopg2://root:pass@localhost/mydb")


def get_db_session():
    return Session(bind=engine)
