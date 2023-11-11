from sqlalchemy import MetaData, Table, Integer, String, Column, ForeignKey


metadata = MetaData()

user_table = Table(
    "User",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50), nullable=False),
    Column("character_id", ForeignKey("Character.id"), nullable=True)
)

character_table = Table(
    "Character",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50), nullable=False)
)

