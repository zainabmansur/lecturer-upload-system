from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, nullable=False)  # "lecturer" or "student"
    created_at = Column(DateTime(timezone=True))

class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)       # stored name (unique on disk)
    original_name = Column(String, nullable=False)  # original user filename
    description = Column(String, nullable=True)
    mime_type = Column(String, nullable=False)
    size = Column(Integer, nullable=False)          # bytes
    uploader_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    upload_time = Column(DateTime(timezone=True) )
    updated_time = Column(DateTime(timezone=True))