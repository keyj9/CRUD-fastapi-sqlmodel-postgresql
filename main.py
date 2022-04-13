from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from sqlmodel import Session, select

from db import engine
from models import Book

app = FastAPI(debug=True)

session = Session(bind=engine)


@app.get('/books')
async def get_all_books():
    statement = select(Book)
    results = session.exec(statement).all()
    return results


@app.post('/books', response_model=Book, status_code=status.HTTP_201_CREATED)
async def create_a_book(book: Book):
    new_book = Book(title=book.title, description=book.description)
    session.add(new_book)
    session.commit()

    return new_book


@app.get('/book/{book_id}', response_model=Book)
async def get_a_book(book_id: int):
    statement = select(Book).where(Book.id == book_id)
    result = session.exec(statement).first()

    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return result


@app.put('/book/{book_id}')
async def get_all_books(book_id: int, book: Book):
    statement = select(Book).where(Book.id == book_id)
    result = session.exec(statement).first()

    result.title = book.title
    result.description = book.description

    session.commit()
    return result


@app.delete('/book/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_a_book(book_id: int):
    statement = select(Book).where(Book.id == book_id)
    result = session.exec(statement).one_or_none()
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="resources not found")

    session.delete(result)
    return result
