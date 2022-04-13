from sqlmodel import SQLModel

from db import engine

print("creating database")

SQLModel.metadata.create_all(engine)
