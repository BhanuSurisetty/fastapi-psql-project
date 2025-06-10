from sqlalchemy.orm import Session
from . import models 
from .models import User
from . import shemas
from .shemas import UserCreate
from fastapi import HTTPException

def get_users_by_email(db: Session, email: str):
    return db.query(User).filter(User.email== email).first()

def create_user(db: Session, user: UserCreate):
    existing_user = get_users_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    # Create a new user instance
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(User).all()
