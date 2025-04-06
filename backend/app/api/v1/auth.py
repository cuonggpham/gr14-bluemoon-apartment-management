from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserOut
from app.services import auth_service
from app.dependencies.db import get_db

router = APIRouter()

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return auth_service.register(user, db)

@router.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    return auth_service.login(user, db)
