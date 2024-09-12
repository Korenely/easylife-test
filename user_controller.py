from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from models import User
from schemas import UserCreate
from database import get_db

router = APIRouter()


@router.post("/users/")
def add_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user.id


@router.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/users/")
def get_all_users(db: Session = Depends(get_db)):
    return db.query(User).all()
