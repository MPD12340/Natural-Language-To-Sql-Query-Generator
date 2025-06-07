from pydantic import BaseModel
from typing import List, Optional


class AuthorBase(BaseModel):
    name: str
    bio: Optional[str] = None


class AuthorCreate(AuthorBase):
    pass


class AuthorOut(AuthorBase):
    id: int
    books: List["BookOut"] = []

    class Config:
        from_attributes = True


class BookBase(BaseModel):
    title: str
    description: Optional[str] = None
    year: Optional[str] = None


class BookCreate(BookBase):
    author_id: int


class BookOut(BookBase):
    id: int

    class Config:
        from_attributes = True


class NaturalStatement(BaseModel):
    text: str


AuthorOut.model_rebuild()
