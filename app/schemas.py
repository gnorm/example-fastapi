from ast import alias
from dataclasses import Field
from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from typing import Optional
from pydantic.types import conint


# Creating a class that uses a pydantic model to validate information that the end user provides. This makes sure the input is valid.
class PostBase(BaseModel):
    video_time: Optional[str] = '-'
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    video_time: str
    id: int
    email: EmailStr
    created_at: datetime
    
    class Config:
        orm_mode = True

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut  
    
    # This class converts the Alchemy model to a pydantic model. See pydantic documentation
    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    video_time: str
    email: EmailStr
    password: str
   
class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class Vote(BaseModel):
    post_id: int
    dir: conint(ge=0, le=1)

