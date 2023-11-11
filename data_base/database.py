from .model import user_table
from sqlalchemy import create_engine, text, insert, select
from sqlalchemy.ext.asyncio import async_sessionmaker


engine = create_engine(
    url="postgresql+psycopg2://postgres:787898@localhost/TG_BOT",
    echo=True
)

session = async_sessionmaker(engine)


def new_user(user_id, user_name):
    with engine.connect() as conn:
        statement = insert(user_table).values(
            {"id": user_id,
             "name": user_name}
        )
        conn.execute(statement)
        conn.commit()


def get_user_by_id(id: int):
    with engine.connect() as conn:
        statement = select(user_table).where(user_table.c.id == id)
        res = conn.execute(statement)
        return res.fetchall()

