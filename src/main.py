from fastapi import FastAPI, Depends
from src.schemas.nlsql_schema import (
    BookCreate,
    BookOut,
    AuthorCreate,
    AuthorOut,
    NaturalStatement,
)
from src.db.db_connection import get_db
from sqlalchemy.orm import Session
from src.models.nlsql_model import Book, Author
from src.prompts.nltosql_prompts import nl_to_sql_prompt
from sqlalchemy import text


app = FastAPI()


@app.post("/books/", response_model=BookOut)
async def create_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


@app.post("/authors/", response_model=AuthorOut)
async def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    db_author = Author(**author.model_dump())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


@app.post("/nl_to_sql/")
async def nl_to_sql(nl_payload: NaturalStatement, db: Session = Depends(get_db)):
    sql_query = nl_to_sql_prompt(nl_payload.text)
    print("Generated SQL:", sql_query)

    try:
        result = db.execute(text(sql_query)).mappings().all()
        return {"query": sql_query, "results": [dict(row) for row in result]}
    except Exception as e:
        return {"query": sql_query, "error": str(e)}
