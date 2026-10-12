from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session, joinedload
from starlette import status

from deps import get_db
from helpers import paginate
from models import Author
from schemas import *

router = APIRouter(prefix="/api/authors", tags=["authors"])

@router.post(
    "/",
    response_model= AuthorOut,
    status_code=status.HTTP_201_CREATED
)
def create_author(
        payload: AuthorCreate,
        db: Session = Depends(get_db),
):
    if db.query(Author).filter_by(name=payload.name).first() is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Author {payload.name} already exists",)

    author = Author(
        name=payload.name.strip(),
    )
    db.add(author)
    db.commit()
    db.refresh(author)
    return author


@router.get(
    "/",
    response_model= dict,
    status_code=status.HTTP_200_OK,
)
def get_authors(
        q:Optional[str] = Query(None,),
        order:str = Query('name'),
        page:int = Query(1, ge=1),
        size:int = Query(10, ge=1, le=100),
        db: Session = Depends(get_db),
):
    query = db.query(Author).options(joinedload(Author.books))
    if q:
        query = query.filter(Author.name.ilike(f"%{q}%"))
    allowed = {'name', 'id'}
    if order.lstrip('-') not in allowed:
        order = 'name'

    col = getattr(Author, order.lstrip('-'))
    if order.startswith('-'):
        col = col.desc()
    query = query.order_by(col)

    data = paginate(query, page=page, size=size)
    data['results'] = [AuthorOut.model_validate(a) for a in data['results']]
    return data

@router.get(
    "/{author_id}",
    response_model= AuthorOut,
    status_code=status.HTTP_200_OK,
)
def get_author(
        author_id: int,
        db: Session = Depends(get_db),
):
    author = db.query(Author).options(joinedload(Author.books)).filter(Author.id == author_id).first()
    if not author:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Author {author_id} does not exist",
        )
    return author