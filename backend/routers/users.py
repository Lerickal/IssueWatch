from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import schemas, crud, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    
    try:
        yield db
    finally:
        db.close
        
@router.get("/users", response_model=list[schemas.UserOut])
def list_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@router.post("/users", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_emaill(db, user.emaill)
    
    if db_user:
        raise HTTPException(status_code=400, detail="Email address already exists")
    
    return crud.create_user(db, user)

@router.get("/users/{user_id}", response_model=schemas.UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    
    if not user:
        raise HTTPException(status_code=404, detail="User Not Found")
    
    return user
