from datetime import date

from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str
    role: int

class Author(BaseModel):
    first_name: str
    last_name: str

class Book(BaseModel):
    title: str
    author: Author
    price: float
    date_published: date = None
