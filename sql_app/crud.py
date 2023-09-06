from sqlalchemy.orm import Session

from sql_app import models, schemas
from sql_app.models import User
from sql_app.schemas import UserCreate, UserUpdate


def create_user(db: Session, user: UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def update_user(db: Session, user_id: int, updated_user: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        for field, value in updated_user.dict().items():
            setattr(db_user, field, value)

        db.commit()
        db.refresh(db_user)

        return db_user



