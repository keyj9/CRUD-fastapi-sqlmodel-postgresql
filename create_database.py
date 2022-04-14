from sqlmodel import SQLModel
from models import Book
from db import engine

print("creating database")

SQLModel.metadata.create_all(engine)
