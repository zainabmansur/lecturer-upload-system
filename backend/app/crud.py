from sqlalchemy.orm import Session
from app import models, schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ---------- User ----------
def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_pw = pwd_context.hash(user.password)
    db_user = models.User(
        email=user.email,
        username=user.username,
        hashed_password=hashed_pw,
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# ---------- File ----------
def get_file(db: Session, file_id: int):
    return db.query(models.File).filter(models.File.id == file_id).first()

def get_files(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.File).offset(skip).limit(limit).all()

def create_file(db: Session, file_data: schemas.FileCreate, stored_name: str,
                original_name: str, mime_type: str, size: int, uploader_id: int):
    db_file = models.File(
        filename=stored_name,
        original_name=original_name,
        description=file_data.description,
        mime_type=mime_type,
        size=size,
        uploader_id=uploader_id
    )
    db.add(db_file)
    db.commit()
    db.refresh(db_file)
    return db_file

def update_file(db: Session, file_id: int, file_update: schemas.FileUpdate):
    db_file = get_file(db, file_id)
    if not db_file:
        return None
    update_data = file_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_file, key, value)
    db.commit()
    db.refresh(db_file)
    return db_file

def delete_file(db: Session, file_id: int):
    db_file = get_file(db, file_id)
    if db_file:
        db.delete(db_file)
        db.commit()
        return True
    return False