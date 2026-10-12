from typing import Optional
from pydantic import BaseModel, Field, ConfigDict, EmailStr

from models import Role


class BookCreate(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    pages: int = Field(ge=1)
    author_id: int

class BookUpdate(BaseModel):
    title: Optional[str] = Field(
        min_length=1,
        max_length=255,
        default=None)
    pages: Optional[int] = Field(ge=1, default=None)
    author_id: Optional[int] = None

class BookOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    pages: int
    author_id: int

class AuthorCreate(BaseModel):
    name: str = Field(min_length=1, max_length=255)

class AuthorUpdate(BaseModel):
    name: str = Field(min_length=1, max_length=255)

class AuthorOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    books: list[BookOut] = []


class UserRegister(BaseModel):
    email:EmailStr
    password: str = Field(min_length=6, max_length=128)
    role:Optional[Role] = Role.user

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    email: EmailStr
    role: Role
    is_active: bool


class TokenOut(BaseModel):
    access_token: str
    token_type: str = "Bearer"
