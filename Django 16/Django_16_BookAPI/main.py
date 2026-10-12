from fastapi import FastAPI

from database import Base, engine
from routers import authors_router, books_router, auth_router

Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="Books API",
    version="1.0",
    description="Books API developed by Zamanoff",
)

app.include_router(authors_router)
app.include_router(books_router)
app.include_router(auth_router)



