from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from deps import require_roles, get_db
from models import Role, Author, Book
from schemas import *

router = APIRouter(prefix="/api/books", tags=["books"])

@router.post("/",
             dependencies=[Depends(require_roles(Role.admin))],
             response_model=BookOut,
             status_code=status.HTTP_201_CREATED
             )
def create_book(
        payload:BookCreate,
        db: Session = Depends(get_db),
):
    author = db.query(Author).filter(Author.id == payload.author_id).first()
    if author is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Author does not exist"
        )
    book = Book(
        title=payload.title.strip(),
        pages=payload.pages,
        author_id=author.id,
    )
    db.add(book)
    db.commit()
    db.refresh(book)
    return book