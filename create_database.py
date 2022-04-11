from sqlmodel import SQLModel
from models import Book
from db import engine

print("creatin database")

SQLModel.metadata.create_all(engine)
