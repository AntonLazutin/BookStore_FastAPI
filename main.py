from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

app = FastAPI()


class Book(BaseModel):
    title: str
    author: str
    price: float
    date_published: date = None


@app.get('/')
def read_root():
    return {"hello": "world"}


@app.get('/items/{item_id}')
def get_book(book_id: int, q : Union[str, None] = None):
    return {'book_id: ' : book_id, 'q': q}