from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from auth import get_current_support_user
import schemas, crud, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    
    try:
        yield db
    finally:
        db.close()
        
@router.get("/issues", response_model=list[schemas.IssueOut])
def list_issues(db: Session = Depends(get_db)):
    return crud.get_issues(db)

@router.post("/issues", response_model=schemas.IssueOut)
def create_issue(issue: schemas.IssueCreate, db: Session = Depends(get_db)):
    return crud.create_issue(db, issue)

@router.put("/issues/{issue_id}", response_model=schemas.IssueOut)
def update_issue(issue_id: int, status: str, db: Session = Depends(get_db), 
                 current_user = Depends(get_current_support_user)):
    return crud.update_issue_status(db, issue_id, status)

@router.get("/issues/my", response_model=list[schemas.IssueOut])
def list_my_issues(db: Session = Depends(get_db), current_user= Depends(get_current_support_user)):
    return crud.get_issues_by_support(db, current_user.id)
