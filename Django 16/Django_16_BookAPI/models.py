from enum import Enum

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy import Enum as SAEnum

from database import Base


class Role(str, Enum):
    admin = "admin"
    user = "user"

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    books = relationship(
        "Book",
        back_populates="author",
        cascade="all, delete, delete-orphan",
    )

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    pages = Column(Integer, nullable=False, default=1)
    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)
    author = relationship(
        "Author",
        back_populates="books"
    )

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False, unique=True, index=True)
    password_hash = Column(String(255), nullable=False)
    role = Column(SAEnum(Role), nullable=False, default=Role.user)
    is_active = Column(Boolean, nullable=False, default=True)