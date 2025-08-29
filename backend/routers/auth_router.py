from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from auth import verify_password, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
import crud, database, schemas, models
from datetime import timedelta

router = APIRouter()

def get_db():
    db = database.SessionLocal()
     
    try:
        yield db
    finally:
        db.close()
        
@router.post("/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.get_user_by_emaill(db, form_data.username)
    if not user or not user.password:
        raise HTTPException(status_code=400, detail="Invalid Credentials")
    if not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=400, detail="Invalid Credentials")
    if user.role != models.UserRole.support:
        raise HTTPException(status_code=403, detail="Only Support Staff can log in")
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.emaill}, expires_delta=access_token_expires)
    
    return {"access_token": access_token, "token_type": "bearer"}