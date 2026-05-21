from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# User schemas
class UserBase(BaseModel):
    email: EmailStr
    username: str
    role: str

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

# Token schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

# File schemas
class FileBase(BaseModel):
    description: Optional[str] = None

class FileCreate(FileBase):
    pass

class FileUpdate(FileBase):
    original_name: Optional[str] = None
    description: Optional[str] = None

class FileOut(FileBase):
    id: int
    filename: str               # stored name
    original_name: str
    mime_type: str
    size: int
    uploader_id: int
    upload_time: datetime
    updated_time: Optional[datetime]

    class Config:
        from_attributes = True