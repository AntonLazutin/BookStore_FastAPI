from typing import Union
from enum import Enum
from datetime import date

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Book Store"
)


class Author(BaseModel):
    first_name: str
    last_name: str

class Book(BaseModel):
    title: str
    author: Author
    price: float
    date_published: date = None


books = [
    {
        "title" : "Вино из одуванчиков",
        "author" : "Рэй Бредбери",
        "price": "2.99",
        "date_published" : "1957-06-22"
    },
]


@app.get('/books')
def get_books():
    return books


@app.post('/books')
def create_book(book: Book):
    try:
        books.append(book)
    except Exception as e:
        return {"error" : str(e)}
    return book


# @app.get('/books/{book_id}')
# def get_book(book_id: int, q : Union[str, None] = None):
#     return books[]

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)