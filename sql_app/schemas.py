from datetime import date
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    name: str
    email: str
    value: float
    created_at: date

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    value: Optional[float] = None

class User(UserBase):
    id: UUID
    name: str
    value: float
    created_at: date


    class Config:
        from_attributes = True